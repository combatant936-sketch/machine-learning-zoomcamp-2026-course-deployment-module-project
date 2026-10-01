# Customer Churn Prediction API

Built and deployed a production-ready **Customer Churn Prediction** REST API as part of the **ML Zoomcamp 2026 — Deployment Module**.

The service takes a telecom customer's profile as input and returns the churn probability along with a binary churn decision, helping businesses proactively retain at-risk customers.

---

## 📌 Project Overview

| Field              | Details                                  |
|--------------------|------------------------------------------|
| **Completed by**   | Muhammad Waqas Khan                      |
| **Course**         | ML Zoomcamp 2026 by DataTalks.Club       |
| **Module**         | Deployment Module                        |

---

## 🛠️ Tech Stack

- **Python 3.12**
- **Scikit-learn** — Model training & evaluation
- **FastAPI + Uvicorn** — REST API server
- **Pydantic** — Request/response validation
- **Pickle** — Model serialization
- **Docker** — Containerized deployment
- **uv** — Dependency management & reproducible builds

---

## 🧠 Model Details

- **Algorithm:** Logistic Regression (`C=1.0`)
- **Validation:** 5-Fold Cross-Validation
- **Metric:** AUC-ROC score
- **Features used:**
  - Categorical: `gender`, `seniorcitizen`, `partner`, `dependents`, `phoneservice`, `multiplelines`, `internetservice`, `onlinesecurity`, `onlinebackup`, `deviceprotection`, `techsupport`, `streamingtv`, `streamingmovies`, `contract`, `paperlessbilling`, `paymentmethod`
  - Numerical: `tenure`, `monthlycharges`, `totalcharges`

---

## 🚀 API Endpoint

### `POST /predict`

**Request body:**
```json
{
  "gender": "female",
  "seniorcitizen": 0,
  "partner": "yes",
  "dependents": "no",
  "phoneservice": "yes",
  "multiplelines": "no",
  "internetservice": "fiber_optic",
  "onlinesecurity": "no",
  "onlinebackup": "no",
  "deviceprotection": "no",
  "techsupport": "no",
  "streamingtv": "yes",
  "streamingmovies": "yes",
  "contract": "month-to-month",
  "paperlessbilling": "yes",
  "paymentmethod": "electronic_check",
  "tenure": 1,
  "monthlycharges": 85.0,
  "totalcharges": 85.0
}
```

**Response:**
```json
{
  "churn_probability": 0.812,
  "churn": true
}
```

---

## 🐳 Running with Docker

**Build the image:**
```bash
docker build -t churn-prediction .
```

**Run the container:**
```bash
docker run -p 9696:9696 churn-prediction
```

**Access the API docs:**
```
http://localhost:9696/docs
```

---

## ⚙️ Running Locally (with uv)

**Install dependencies:**
```bash
uv sync --locked
```

**Start the server:**
```bash
uvicorn src.machine_learning_zoomcamp_2026_course_deployment_module_project.app:app --host 0.0.0.0 --port 9696
```

---

## 🧪 Running Tests

```bash
uv run python -m src.machine_learning_zoomcamp_2026_course_deployment_module_project.test
```

---

## 📁 Project Structure

```
├── src/
│   └── machine_learning_zoomcamp_2026_course_deployment_module_project/
│       ├── app.py          # FastAPI application & /predict endpoint
│       ├── models.py       # Pydantic request/response models
│       ├── train.py        # Model training & serialization script
│       ├── test.py         # API test script
│       ├── ping.py         # Health check script
│       └── model_C=1.0.bin # Serialized trained model
├── Dockerfile
├── pyproject.toml
├── uv.lock
└── README.md
```
