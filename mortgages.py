import streamlit as st
import pandas as pd
import numpy as np


# Setup Sidebar
st.sidebar.markdown("# Assumptions")
st.sidebar.markdown("## Mortgage")

mortgage_remaining = st.sidebar.number_input(
    'Mortgage Remaining', value=178850, min_value=0)

term_remaining = st.sidebar.number_input(
    'Term Remaining', value=35, min_value=0)

st.sidebar.markdown("## HTB")

variable_rate = st.sidebar.number_input(
    'Variable Rate after Fixed-term expires', value=6.7, min_value=0.0)


"""
# Mortgage Options

How on earth do you choose? Well, we calculate to see which one makes the most sense.

---

## Options

### A: 5-year Fixed, No HTB payment
### B: 3-year Fixed, 50% HTB payment
### C: 3-year Fixed, 100% HTB payment

"""

options = {
    "a": {
        "interest_rate": 2.2,
        "term_length": 5,
        "HTB_redemption": 0
    },
    "b": {
        "interest_rate": 2.2,
        "term_length": 5,
        "HTB_redemption": 0
    }
}

options

mortgage_remaining
