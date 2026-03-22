import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    """Load and cache the dataset"""
    df = pd.read_csv("cleaned_df.csv")
    return df

def get_column_mapping():
    """Return column name mapping"""
    return {
        'area': 'total_sqft',
        'price': 'price',
        'bhk': 'bhk',
        'bath': 'bath',
        'location': 'location',
        'encoded_loc': 'encoded_loc'
    }