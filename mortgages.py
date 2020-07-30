import streamlit as st
import pandas as pd
import numpy as np
from mortgage import Loan
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

htb_amount = st.sidebar.number_input(
    'Loan Value', value=155000, min_value=0)


# Functions
def mortgage_df(interest):

    rng = pd.date_range(
        start_date, periods=payments_per_year * term_remaining, freq='MS')

    rng.name = "Payment Date"
    df = pd.DataFrame(index=rng, columns=[
        'Payment', 'Principal Paid', 'Interest Paid', 'Ending Balance'], dtype='float')
    df.reset_index(inplace=True)
    df.index += 1
    df.index.name = "Period"

    loan = Loan(principal=mortgage_remaining, interest=interest /
                100, term=term_remaining, currency='£')

    for period in range(1, len(df)+1):
        schedule = loan.schedule(period)
        df.loc[period, 'Payment'] = round(schedule.payment, 2)
        df.loc[period, 'Ending Balance'] = round(schedule.balance, 2)
        df.loc[period, 'Interest Paid'] = round(schedule.total_interest, 2)
        df.loc[period, 'Principal Paid'] = round(
            mortgage_remaining - schedule.balance, 2)

    df = df.round(2)

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
        "interest_rate": 0.2,
        "fixed_term_length": 5,
        "HTB_redemption_percentage": 0
    },
    "b": {
        "interest_rate": 2.2,
        "fixed_term_length": 5,
        "HTB_redemption_percentage": 0
    },
    "c": {
        "interest_rate": 3.2,
        "fixed_term_length": 5,
        "HTB_redemption_percentage": 0
    }
}

'Options', options

"""
---
# Help To Buy
"""


"""
---
# Option A
"""

df_A = mortgage_df(options['a']['interest_rate'])
df_A

"""
---
# Option B
"""

df_B = mortgage_df(options['b']['interest_rate'])
df_B


"""
---
# Option C
"""

df_C = mortgage_df(options['c']['interest_rate'])
df_C

"""
---
"""

loan = Loan(principal=200000, interest=.06, term=30)
loan

loan.schedule(1).payment
loan.schedule(2).payment
loan.schedule(3).payment
