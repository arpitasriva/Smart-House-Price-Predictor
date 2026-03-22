import pickle
import streamlit as st
import time

@st.cache_resource
def load_model():
    """Load and cache the machine learning model"""
    with st.spinner('🔄 Loading AI Model...'):
        time.sleep(0.5)
        with open("RF_model.pkl", "rb") as file:
            model = pickle.load(file)
    return model