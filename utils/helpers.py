import pandas as pd
import streamlit as st

def get_encoded_location(location, df, col_mapping):
    """Get encoded value for a location"""
    location_encoding = dict(zip(
        df[col_mapping['location']], 
        df[col_mapping['encoded_loc']]
    ))
    return location_encoding.get(location, None)

def calculate_price_adjustment(condition, parking, garden, security, renovation, age):
    """Calculate price adjustment based on features"""
    adjustment = 1.0
    
    condition_multipliers = {
        "Needs Work": 0.85,
        "Average": 0.95,
        "Good": 1.0,
        "Excellent": 1.12,
        "Luxury": 1.25
    }
    adjustment *= condition_multipliers.get(condition, 1.0)
    
    if parking:
        adjustment *= 1.03
    if garden:
        adjustment *= 1.02
    if security:
        adjustment *= 1.02
    if renovation:
        adjustment *= 1.05
    if age < 2:
        adjustment *= 1.04
    elif age > 20:
        adjustment *= 0.92
    
    return adjustment

def format_price(price):
    """Format price in lakhs and crores"""
    lakhs = price / 100000
    crores = price / 10000000
    return lakhs, crores