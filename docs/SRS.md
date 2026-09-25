# Software Requirements Specification (SRS)

**Project:** Dynamic Rental Price Prediction through Multi-Platform Data Scraping, Exploratory Data Analysis, Ensemble Machine Learning and Explainable AI

**Version:** 1.0
**Date:** 2026-09-25
**Status:** Draft

---

## 1. Introduction

### 1.1 Purpose

This document specifies the functional and non-functional requirements for a rental-price intelligence system that predicts residential rental prices and explains predictions using Explainable AI (SHAP).

### 1.2 Scope

The system will:

- Collect publicly available rental listing data from multiple online platforms.
- Clean, integrate, and transform the data into an analysis-ready format.
- Train and evaluate five regression models on the processed data.
- Select the best-performing model based on standard evaluation metrics.
- Generate SHAP-based explanations for individual predictions.
- Expose an interactive Streamlit web interface for end-user predictions.

### 1.3 Definitions & Acronyms

| Term | Definition |
|------|-----------|
| EDA | Exploratory Data Analysis |
| SHAP | SHapley Additive exPlanations |
| XAI | Explainable Artificial Intelligence |
| MAE | Mean Absolute Error |
| RMSE | Root Mean Squared Error |
| MAPE | Mean Absolute Percentage Error |
| R² | Coefficient of Determination |
| BHK | Bedroom, Hall, Kitchen configuration |

---

## 2. Overall Description

### 2.1 Product Perspective

This is a standalone analytical system. It is **not** a production SaaS platform; it is a research-oriented capstone project demonstrating the full ML lifecycle from data collection to explainable deployment.

### 2.2 User Classes

| User | Description |
|------|-------------|
| Tenant / Buyer | Enters property details, receives a predicted price and explanation. |
| Landlord / Agent | Uses the tool to benchmark listing prices. |
| Evaluator / Faculty | Reviews the methodology, code, and results. |

### 2.3 Operating Environment

- Python 3.10+
- Any modern web browser (for Streamlit UI)
- Windows / Linux / macOS

---

## 3. Functional Requirements

### FR-01: Data Ingestion

| Field | Detail |
|-------|--------|
| ID | FR-01 |
| Description | The system shall ingest rental listing data from at least two publicly available sources. |
| Input | Raw CSV/JSON/API responses. |
| Output | Unified raw dataset stored in `data/raw/`. |
| Priority | High |

### FR-02: Data Cleaning & Preprocessing

| Field | Detail |
|-------|--------|
| ID | FR-02 |
| Description | The system shall handle missing values, duplicates, data-type mismatches, and outliers. |
| Input | Raw dataset. |
| Output | Cleaned dataset stored in `data/processed/`. |
| Priority | High |

### FR-03: Exploratory Data Analysis

| Field | Detail |
|-------|--------|
| ID | FR-03 |
| Description | The system shall produce summary statistics, distribution plots, correlation matrices, and outlier analysis. |
| Input | Cleaned dataset. |
| Output | Jupyter notebook with visualisations. |
| Priority | High |

### FR-04: Feature Engineering

| Field | Detail |
|-------|--------|
| ID | FR-04 |
| Description | The system shall create derived features (e.g., price-per-sqft, locality encoding, amenity score) and encode categorical variables. |
| Input | Cleaned dataset. |
| Output | Feature-engineered dataset stored in `data/processed/`. |
| Priority | High |

### FR-05: Model Training

| Field | Detail |
|-------|--------|
| ID | FR-05 |
| Description | The system shall train Linear Regression, Decision Tree, Random Forest, XGBoost, and CatBoost regressors. |
| Input | Feature-engineered dataset (train split). |
| Output | Trained model objects serialised via Joblib. |
| Priority | High |

### FR-06: Model Evaluation & Selection

| Field | Detail |
|-------|--------|
| ID | FR-06 |
| Description | The system shall evaluate all models using MAE, RMSE, MAPE, and R², then select the best. |
| Input | Trained models + test split. |
| Output | Comparison table / chart; best model identifier. |
| Priority | High |

### FR-07: SHAP Explainability

| Field | Detail |
|-------|--------|
| ID | FR-07 |
| Description | The system shall generate SHAP summary plots and per-prediction force/waterfall plots for the best model. |
| Input | Best trained model + input features. |
| Output | SHAP visualisations embedded in notebook and Streamlit app. |
| Priority | High |

### FR-08: Streamlit Prediction App

| Field | Detail |
|-------|--------|
| ID | FR-08 |
| Description | The system shall serve a web UI where a user inputs property details and receives a predicted price with SHAP explanation. |
| Input | User-provided property attributes. |
| Output | Predicted rent (₹), feature importance chart, SHAP waterfall plot. |
| Priority | Medium |

---

## 4. Non-Functional Requirements

| ID | Requirement | Target |
|----|-------------|--------|
| NFR-01 | **Performance** — Prediction latency | < 2 seconds per prediction |
| NFR-02 | **Accuracy** — Best model R² on test set | ≥ 0.75 |
| NFR-03 | **Usability** — Streamlit UI understandable without training | Yes |
| NFR-04 | **Portability** — Runs on Windows, Linux, macOS | Yes |
| NFR-05 | **Reproducibility** — Pinned dependencies, random seeds | Yes |
| NFR-06 | **Maintainability** — Modular `src/` code, documented functions | Yes |

---

## 5. Data Flow Diagram

```
 ┌──────────┐     ┌───────────┐     ┌─────┐     ┌─────────┐
 │ Sources  │ ──► │ Ingestion │ ──► │ EDA │ ──► │ Feature │
 └──────────┘     └───────────┘     └─────┘     │  Eng.   │
                                                 └────┬────┘
                                                      │
                         ┌────────────────────────────┘
                         ▼
                  ┌─────────────┐     ┌──────────┐     ┌──────────┐
                  │  Training   │ ──► │ Evaluate │ ──► │  SHAP    │
                  └─────────────┘     └──────────┘     └─────┬────┘
                                                             │
                                                             ▼
                                                      ┌──────────┐
                                                      │ Streamlit│
                                                      └──────────┘
```

---

## 6. Constraints & Assumptions

1. Data is collected only from **publicly available** sources — no proprietary APIs requiring paid access.
2. The system targets the **Indian residential rental market**; currency is ₹ (INR).
3. The project is scoped as a **capstone demonstration**, not a production service.
4. Model retraining is manual (no automated retraining pipeline in v1).

---

## 7. Acceptance Criteria

| Criterion | Condition |
|-----------|-----------|
| AC-01 | At least 1 000 cleaned rental records in the final dataset. |
| AC-02 | All five models trained and evaluation metrics reported. |
| AC-03 | SHAP explanations generated for the best model. |
| AC-04 | Streamlit app loads, accepts input, returns prediction + explanation. |
| AC-05 | Code is version-controlled on GitHub with meaningful commit history. |

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-09-25 | Team | Initial draft. |
