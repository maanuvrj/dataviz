import pandas as pd
import streamlit as st

myDataframe = pd.DataFrame({
    'srno': [1, 2, 3, 4, 5],
    'gender': ['m', 'f', 'f', 'm', 'm'],
    'weight': [50, 55, 60,70, 75],
    'height': [5.5, 5.7, 5.8, 5.9, 6.2]},
    )

st.table(myDataframe)
st.line_chart(myDataframe)