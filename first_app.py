import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

"""
# My first app
Here's our first attempt at using data to create a table:

There's lots more where this comes from

"""

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df

"""
---
"""

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

"""
---
"""

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


"""
---
"""


x = 10
'x', x

"""
---
"""

st.button('Say hello')

agree = st.checkbox('I agree')
if agree:
    st.write('Great!')
