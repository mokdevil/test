import streamlit as st
import pandas as pd

st.title("File read test")
st.write("Choose a text/image file to display")

uploaded_file = st.file_uploader("Choose a file...")

