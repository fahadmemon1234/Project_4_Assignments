# -*- coding: utf-8 -*-
"""08_Build_Data_Driven.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ly-FTNl8ye-3UFcmxbiD0-SlzqpwV5OE?usp=sharing
"""

# !pip install streamlit pyngrok --quiet

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
import streamlit as st
import pandas as pd
import numpy as np
 
 
st.title("🚀 Streamlit Crash Course")


st.sidebar.title("Settings")
selected_chart = st.sidebar.selectbox("Choose Chart Type", ["Line", "Bar"])


name = st.text_input("Enter your name:", "")
if name:
    st.success(f"Welcome, {name}!")


data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['A', 'B', 'C']
)

st.subheader("📊 Data Preview")
st.write(data)


st.subheader("📈 Visualization")
if selected_chart == "Line":
    st.line_chart(data)
else:
    st.bar_chart(data)


# from pyngrok import ngrok


# ngrok.kill()

# # !streamlit run app.py &

# public_url = ngrok.connect(port=8501)
# print("Streamlit app is live at:", public_url)