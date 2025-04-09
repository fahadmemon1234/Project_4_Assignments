# -*- coding: utf-8 -*-
"""09_Country_Information_Cards.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FnwIsLVtRvT12YInMKfvD-7XfwgNjL70?usp=sharing
"""

# !pip install streamlit pyngrok requests --quiet

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
import streamlit as st
import requests

st.set_page_config(page_title="Country Info Cards", layout="centered")
st.title("🌍 Country Information Cards")

country = st.text_input("Enter Country Name", "Pakistan")

if country:
    url = f"https://restcountries.com/v3.1/name/{country}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]
        name = data['name']['common']
        capital = data.get('capital', ['N/A'])[0]
        region = data.get('region', 'N/A')
        population = data.get('population', 'N/A')
        flag = data.get('flags', {}).get('png', '')

        st.markdown(f"""
        <div style='border:1px solid #ddd;padding:20px;border-radius:10px;box-shadow:2px 2px 10px #ccc;text-align:center;'>
            <h2>{name}</h2>
            <img src="{flag}" width="150"/>
            <p><strong>Capital:</strong> {capital}</p>
            <p><strong>Region:</strong> {region}</p>
            <p><strong>Population:</strong> {population:,}</p>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.error("Country not found! Please check the spelling.")


# from pyngrok import ngrok

# ngrok.kill()

# !streamlit run app.py &

# public_url = ngrok.connect(port=8501)
# print("🔗 Click to open Streamlit App:", public_url)