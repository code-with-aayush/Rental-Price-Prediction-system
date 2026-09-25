# Dynamic Rental Price Prediction through Multi-Platform Data Scraping, Exploratory Data Analysis, Ensemble Machine Learning and Explainable AI

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Problem Statement

Rental markets are highly fragmented — listings are scattered across multiple platforms with inconsistent formats, missing attributes, and opaque pricing. Tenants lack a reliable way to judge whether a listed rent is fair, and landlords struggle to price competitively. Existing tools rarely explain *why* a price is what it is.

This project addresses three gaps:

1. **Data fragmentation** — consolidating rental listings from multiple public sources into a unified dataset.
2. **Price opacity** — predicting rental prices using ensemble machine-learning models trained on real market data.
3. **Lack of explainability** — using SHAP (SHapley Additive exPlanations) to show which property features drive each prediction.

---

## Objectives

| # | Objective |
|---|-----------|
| 1 | Collect publicly available rental listing data from multiple online platforms. |
| 2 | Clean, integrate, and preprocess the multi-source data into analysis-ready form. |
| 3 | Perform exploratory data analysis (EDA) to uncover patterns and feature relationships. |
| 4 | Engineer meaningful features (locality encoding, amenity scores, area bins, etc.). |
| 5 | Train and compare multiple regression models (Linear Regression, Decision Tree, Random Forest, XGBoost, CatBoost). |
| 6 | Evaluate models using MAE, RMSE, MAPE, and R² to select the best performer. |
| 7 | Apply SHAP to produce interpretable, per-prediction explanations. |
| 8 | Deploy an interactive Streamlit web application for end-user predictions. |

---

## End-to-End Pipeline

```
Rental Listing Data
       │
       ▼
 ┌─────────────┐
 │  Ingestion  │  ← Multi-platform scraping / API collection
 └──────┬──────┘
        ▼
 ┌─────────────┐
 │  Cleaning   │  ← Deduplication, type casting, missing-value handling
 └──────┬──────┘
        ▼
 ┌─────────────┐
 │    EDA      │  ← Distributions, correlations, outlier detection
 └──────┬──────┘
        ▼
 ┌─────────────┐
 │  Feature    │  ← Encoding, scaling, new derived features
 │  Engineering│
 └──────┬──────┘
        ▼
 ┌─────────────┐
 │  Modelling  │  ← LR, DT, RF, XGBoost, CatBoost
 └──────┬──────┘
        ▼
 ┌─────────────┐
 │  Evaluation  │  ← MAE, RMSE, MAPE, R²
 │  & Tuning    │
 └──────┬──────┘
        ▼
 ┌─────────────┐
 │  Best Model  │  ← Saved via Joblib
 └──────┬──────┘
        ▼
 ┌─────────────┐
 │  SHAP        │  ← Feature importance + per-prediction explanations
 └──────┬──────┘
        ▼
 ┌─────────────┐
 │  Streamlit   │  ← Interactive prediction UI
 │  App         │
 └─────────────┘
```

---

## Tech Stack

| Layer | Technologies |
|-------|-------------|
| Language | Python 3.10+ |
| Data | Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn, Plotly |
| ML | Scikit-learn, XGBoost, CatBoost |
| Explainability | SHAP |
| Deployment | Streamlit |
| Serialisation | Joblib |
| Version Control | Git / GitHub |

---

## Directory Structure

```
rental-price-prediction-xai/
├── data/
│   ├── raw/              # Original, untouched datasets
│   ├── interim/          # Intermediate transformations
│   └── processed/        # Final analysis-ready data
├── notebooks/            # Jupyter notebooks (numbered sequentially)
├── src/
│   ├── ingestion/        # Data collection scripts
│   ├── preprocessing/    # Cleaning & transformation
│   ├── features/         # Feature engineering
│   ├── models/           # Model training, evaluation, tuning
│   └── explainability/   # SHAP analysis
├── app/                  # Streamlit application
├── tests/                # Unit and integration tests
├── docs/                 # SRS, sprint plans, reports
├── models/               # Serialised trained models (.joblib)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Planned Models

| Model | Type | Rationale |
|-------|------|-----------|
| Linear Regression | Baseline | Establishes a simple, interpretable benchmark. |
| Decision Tree | Non-linear | Captures feature interactions without scaling. |
| Random Forest | Ensemble (bagging) | Reduces variance of individual trees. |
| XGBoost | Ensemble (boosting) | State-of-the-art gradient boosting with regularisation. |
| CatBoost | Ensemble (boosting) | Handles categorical features natively; robust to overfitting. |

---

## Evaluation Metrics

| Metric | Formula | Purpose |
|--------|---------|---------|
| MAE | Mean Absolute Error | Average prediction error in original units. |
| RMSE | Root Mean Squared Error | Penalises large errors more heavily. |
| MAPE | Mean Absolute Percentage Error | Scale-independent error measure. |
| R² | Coefficient of Determination | Proportion of variance explained. |

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/<your-username>/rental-price-prediction-xai.git
cd rental-price-prediction-xai

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook notebooks/
```

---

## Current Sprint

**Sprint 1 — Project Planning & Foundation** (see [`docs/SPRINT_1.md`](docs/SPRINT_1.md))

---

## License

This project is developed as a B.Tech final-year capstone. See [LICENSE](LICENSE) for details.

---

## Authors

*Add team member names and roll numbers here.*
aniket singh, aayush prabhakar, aditya varshnay
