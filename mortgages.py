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

payments_per_year = st.sidebar.number_input(
    'Payments per year', value=12, min_value=1)

start_date = st.sidebar.date_input("Start date", value=date(2020, 6, 1))

st.sidebar.markdown("## HTB")

variable_rate = st.sidebar.number_input(
    'Variable Rate after Fixed-term expires', value=6.7, min_value=0.0)


# Functions
def mortgage_df(interest):

    rng = pd.date_range(start_date, periods=term_remaining *
                        payments_per_year, freq='MS')

    rng.name = "Payment Date"

    df = pd.DataFrame(index=rng, columns=[
        'Payment', 'Principal Paid', 'Interest Paid', 'Ending Balance'], dtype='float')
    df.reset_index(inplace=True)
    df.index += 1
    df.index.name = "Period"

    df["Payment"] = -1 * npf.pmt(interest/12, term_remaining *
                                 payments_per_year, mortgage_remaining)

    df["Principal Paid"] = -1 * npf.ppmt(interest/payments_per_year,
                                         df.index, term_remaining * payments_per_year, mortgage_remaining)
    return df


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

"""
---
# Option A
"""

df_A = mortgage_df(2.22)
df_A

"""
---
# Option B
"""

df_B = mortgage_df(3.22)
df_B


"""
---
# Option C
"""

df_C = mortgage_df(2.22)
df_C
