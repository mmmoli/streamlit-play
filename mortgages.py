import streamlit as st
import pandas as pd
import numpy as np
import numpy_financial as npf
from datetime import date


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

# Options

### A: 5-year Fixed, No HTB payment

### B: 3-year Fixed, 50% HTB payment

### C: 3-year Fixed, 100% HTB payment

"""

options = {
    "a": {
        "interest_rate": 2.2,
        "fixed_term_length": 5,
        "HTB_redemption_percentage": 0
    },
    "b": {
        "interest_rate": 2.2,
        "fixed_term_length": 5,
        "HTB_redemption_percentage": 0
    },
    "c": {
        "interest_rate": 2.2,
        "fixed_term_length": 5,
        "HTB_redemption_percentage": 0
    }
}

'Options', options


interest = 0.04
years = 30
payments_year = 12
mortgage = 400000
start_date = (date(2021, 1, 1))


pmt = -1 * npf.pmt(interest/12, years*payments_year, mortgage)

"Monthly payment of", pmt
