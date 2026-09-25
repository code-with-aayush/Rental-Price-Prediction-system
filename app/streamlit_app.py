"""
Streamlit App — Rental Price Prediction with SHAP Explanation.

TODO (Sprint 5):
    - Build input form for property details.
    - Load best serialised model from models/.
    - Display predicted price and SHAP waterfall plot.

Run with:
    streamlit run app/streamlit_app.py
"""

from __future__ import annotations

import streamlit as st


def main() -> None:
    """Entry point for the Streamlit application."""
    st.set_page_config(
        page_title="Rental Price Predictor",
        page_icon="🏠",
        layout="centered",
    )

    st.title("🏠 Rental Price Prediction")
    st.subheader("with Explainable AI (SHAP)")

    st.info(
        "This application is under development.  "
        "The prediction interface will be available after model training is complete (Sprint 5)."
    )

    st.markdown("---")
    st.markdown(
        "**Pipeline:**  Data Collection → Cleaning → EDA → "
        "Feature Engineering → ML Models → SHAP → This App"
    )


if __name__ == "__main__":
    main()
