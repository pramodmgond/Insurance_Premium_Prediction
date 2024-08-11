
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse
from uvicorn import run as app_run

from typing import Optional

from Insurance_Prediction.constants import APP_HOST, APP_PORT
from Insurance_Prediction.pipeline.prediction_pipeline import InsuranceData, InsuranceRegressor
from Insurance_Prediction.pipeline.training_pipeline import TrainPipeline

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory='templates')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.age: Optional[int] = None
        self.bmi: Optional[float] = None
        self.children: Optional[int] = None
        self.region: Optional[str] = None
        self.sex: Optional[str] = None
        self.smoker: Optional[str] = None


    async def get_Insurance_data(self):
        form = await self.request.form()
        self.age = form.get("age")
        self.bmi = form.get("bmi")
        self.children = form.get("children")
        self.region = form.get("region")
        self.sex = form.get("sex")
        self.smoker = form.get("smoker")


@app.get("/", tags=["authentication"])
async def index(request: Request):

    return templates.TemplateResponse(
            "Insurance.html",{"request": request, "context": "Rendering"})


@app.get("/train")
async def trainRouteClient():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()

        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/")
async def predictRouteClient(request: Request):
    try:
        form = DataForm(request)
        await form.get_Insurance_data()
        
        Insurance_data = InsuranceData(
                                age= form.age,
                                bmi = form.bmi,
                                children = form.children,
                                region = form.region,
                                sex= form.sex,
                                smoker= form.smoker
                                )
        
        Insurance_df = Insurance_data.get_insurance_input_data_frame()

        model_predictor = InsuranceRegressor()

        value = model_predictor.predict(dataframe=Insurance_df)[0]

        status = round(value, 2)


        return templates.TemplateResponse(
            "Insurance.html",
            {"request": request, "context": status},
        )
        
    except Exception as e:
        return {"status": False, "error": f"{e}"}


if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)