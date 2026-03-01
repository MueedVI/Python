import streamlit as st
from scipy.stats import norm
import math

st.title("Statistical Power Calculator")

alpha = st.number_input(
    "Alpha (significance level)", value=0.05, min_value=0.0001, max_value=0.5
)
n = st.number_input("Sample size per group (n)", value=100, min_value=1)
effect_size = st.number_input("Effect size (Cohen's d)", value=0.5)

if st.button("Calculate Power"):
    z_alpha = norm.ppf(1 - alpha / 2)
    SE = math.sqrt(2 / n)
    z_effect = effect_size / SE
    beta = norm.cdf(z_alpha - z_effect) - norm.cdf(-z_alpha - z_effect)
    power = 1 - beta
    st.success(f"Beta (Type 2 error): {beta:.4f}\nPower (1 - Beta): {power:.4f}")
