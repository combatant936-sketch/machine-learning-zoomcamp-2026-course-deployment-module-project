import pickle
from fastapi import FastAPI
import uvicorn
from .models import Customer, PredictResponse

app = FastAPI(title="customer-churn-prediction")
with open('src/machine_learning_zoomcamp_2026_course_deployment_module_project/model_C=1.0.bin', 'rb') as f_in:
        dv, model = pickle.load(f_in)


def predict_single(customer):
    X = dv.transform([customer])
    result = model.predict_proba(X)[0, 1]
    return float(result)


@app.post("/predict")
def predict(customer: Customer) -> PredictResponse:
    prob = predict_single(customer.model_dump())

    return {
        "churn_probability": prob,
        "churn": bool(prob >= 0.5)
    }


if __name__ == "__main__":
    uvicorn.run(
        "src.machine_learning_zoomcamp_2026_course_deployment_module_project.app:app",
        host="0.0.0.0",
        port=9696
    )