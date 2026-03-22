import streamlit as st
import time
from utils.data_loader import load_data, get_column_mapping
from utils.model_loader import load_model
from utils.helpers import get_encoded_location, calculate_price_adjustment, format_price

def render_predictor():
    """Render price predictor page with professional color scheme"""
    
    # Custom CSS for all input fields with increased font sizes
    st.markdown("""
    <style>
    /* Global font size increase */
    .stMarkdown, .stText, .stButton, .stSelectbox, .stNumberInput, .stSlider, .stCheckbox {
        font-size: 16px !important;
    }
    
    /* Labels styling - increased font size */
    .stSelectbox label, .stNumberInput label, .stSlider label, .stCheckbox label {
        color: #2c3e50 !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        margin-bottom: 0.5rem !important;
        display: block !important;
    }
    
    /* Dropdown styling */
    .stSelectbox > div > div {
        background-color: white !important;
        border: 2px solid #e0e0e0 !important;
        border-radius: 10px !important;
        color: #2c3e50 !important;
        font-size: 1rem !important;
        padding: 0.5rem !important;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #3498db !important;
        box-shadow: 0 2px 8px rgba(52, 152, 219, 0.1) !important;
    }
    
    .stSelectbox > div > div > div {
        color: #2c3e50 !important;
        font-size: 1rem !important;
    }
    
    /* Dropdown options menu */
    div[data-baseweb="select"] > div {
        font-size: 1rem !important;
    }
    
    /* Number input styling */
    .stNumberInput > div > div > input {
        background-color: white !important;
        border: 2px solid #e0e0e0 !important;
        border-radius: 10px !important;
        color: #2c3e50 !important;
        font-size: 1rem !important;
        padding: 0.75rem 1rem !important;
        width: 100% !important;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #3498db !important;
        box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1) !important;
        outline: none !important;
    }
    
    /* Slider styling */
    .stSlider > div > div > div > div {
        background-color: #3498db !important;
        height: 6px !important;
    }
    
    .stSlider > div > div > div > div > div {
        background-color: #3498db !important;
        width: 18px !important;
        height: 18px !important;
        border: 2px solid white !important;
    }
    
    .stSlider label {
        color: #2c3e50 !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
    }
    
    /* Checkbox styling */
    .stCheckbox {
        background-color: white !important;
        padding: 12px 15px !important;
        border-radius: 10px !important;
        border: 2px solid #e0e0e0 !important;
        margin: 8px 0 !important;
        transition: all 0.3s ease !important;
    }
    
    .stCheckbox:hover {
        border-color: #3498db !important;
        background-color: #f8f9fa !important;
        transform: translateY(-2px) !important;
    }
    
    .stCheckbox label {
        color: #2c3e50 !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
        cursor: pointer !important;
    }
    
    .stCheckbox > div {
        transform: scale(1.1) !important;
    }
    
    /* Select Slider styling */
    .stSelectSlider label {
        color: #2c3e50 !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
    }
    
    /* Container styling */
    .stContainer {
        border: 2px solid #e9ecef !important;
        border-radius: 15px !important;
        padding: 1.5rem !important;
        background-color: white !important;
        margin-bottom: 1.5rem !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
    }
    
    /* Section headers */
    .section-header {
        background: linear-gradient(135deg, #3498db15 0%, #2c3e5015 100%);
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        border-left: 5px solid #3498db;
    }
    
    .section-header h3 {
        color: #2c3e50;
        margin: 0;
        font-size: 1.3rem;
        font-weight: 600;
    }
    
    /* Additional features card */
    .features-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        padding: 1rem;
        border-radius: 12px;
        border: 2px solid #e9ecef;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
    }
    
    .features-card:hover {
        border-color: #3498db;
        box-shadow: 0 4px 12px rgba(52, 152, 219, 0.1);
    }
    
    /* Prediction button styling */
    .stButton > button {
        background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%) !important;
        color: white !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        padding: 0.75rem 2rem !important;
        border-radius: 12px !important;
        border: none !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgba(52, 152, 219, 0.3) !important;
    }
    
    /* Error/Success messages */
    .stAlert {
        font-size: 1rem !important;
        border-radius: 10px !important;
    }
    
    /* Spinner */
    .stSpinner > div {
        font-size: 1rem !important;
    }
    
    /* Increase font size for all text */
    p, div, span, li {
        font-size: 1rem !important;
    }
    
    h1 {
        font-size: 2.5rem !important;
    }
    
    h2 {
        font-size: 2rem !important;
    }
    
    h3 {
        font-size: 1.5rem !important;
    }
    
    /* Tooltip styling */
    .stTooltipIcon {
        color: #3498db !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Page header
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <div style="font-size: 4rem; animation: bounce 2s infinite;">💰</div>
        <h1 style="background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
                   -webkit-background-clip: text;
                   -webkit-text-fill-color: transparent;
                   font-size: 2.8rem;
                   margin: 1rem 0;
                   font-weight: 700;">
            Price Predictor
        </h1>
        <p style="color: #5a6c7e; font-size: 1.2rem;">Enter your property details to get an instant valuation</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data and model
    df = load_data()
    model = load_model()
    col_mapping = get_column_mapping()
    
    # Input section
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        with st.container():
            st.markdown("""
            <div class="section-header">
                <h3>📍 Location & Size</h3>
            </div>
            """, unsafe_allow_html=True)
            
            location = st.selectbox(
                "🏠 Select Location",
                options=sorted(df[col_mapping['location']].unique()),
                key="pred_location",
                help="Choose the property location from the list"
            )
            
            min_area = max(300, int(df[col_mapping['area']].min()))
            max_area = int(df[col_mapping['area']].max())
            default_area = min(1200, (min_area + max_area) // 2)
            
            total_sqft = st.number_input(
                "📐 Total Square Feet",
                min_value=min_area,
                max_value=max_area,
                value=default_area,
                step=50,
                key="pred_area",
                help="Total built-up area in square feet"
            )
    
    with col2:
        with st.container():
            st.markdown("""
            <div class="section-header">
                <h3>🏠 Rooms & Amenities</h3>
            </div>
            """, unsafe_allow_html=True)
            
            bath = st.selectbox(
                "🛁 Number of Bathrooms",
                options=sorted(df[col_mapping['bath']].unique()),
                key="pred_bath",
                help="Total bathrooms in the property"
            )
            bhk = st.selectbox(
                "🏠 BHK Configuration",
                options=sorted(df[col_mapping['bhk']].unique()),
                key="pred_bhk",
                help="Number of bedrooms (BHK = Bedroom Hall Kitchen)"
            )
    
    encoded_loc = get_encoded_location(location, df, col_mapping)
    
    # Additional features
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; margin: 1.5rem 0;">
        <div style="font-size: 2.5rem; animation: float 3s ease-in-out infinite;">✨</div>
        <h3 style="color: #2c3e50; font-size: 1.8rem; margin: 0.5rem 0;">Additional Features</h3>
        <p style="color: #5a6c7e; font-size: 1.1rem;">Enhance your property value with these amenities</p>
    </div>
    """, unsafe_allow_html=True)
    
    col3, col4, col5 = st.columns(3, gap="large")
    
    with col3:
        with st.container():
            st.markdown('<div class="features-card">', unsafe_allow_html=True)
            parking = st.checkbox("🚗 Car Parking", value=True, help="Increases property value by 3%")
            garden = st.checkbox("🌳 Garden", value=False, help="Increases property value by 2%")
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        with st.container():
            st.markdown('<div class="features-card">', unsafe_allow_html=True)
            security = st.checkbox("🔒 24/7 Security", value=False, help="Increases property value by 2%")
            renovation = st.checkbox("🛠️ Recently Renovated", value=False, help="Increases property value by 5%")
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col5:
        with st.container():
            st.markdown('<div class="features-card">', unsafe_allow_html=True)
            condition = st.select_slider(
                "🏠 Condition Rating",
                options=["Needs Work", "Average", "Good", "Excellent", "Luxury"],
                value="Good",
                help="Better condition = Higher value"
            )
            age = st.slider("📅 Age (Years)", min_value=0, max_value=30, value=5, help="Newer properties have higher value")
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Prediction button
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        predict_button = st.button("💸 PREDICT PRICE", use_container_width=True)
    
    # Prediction result
    if predict_button:
        if encoded_loc is None:
            st.error("❌ Location encoding error. Please try again.")
        else:
            with st.spinner('🧠 Analyzing property data...'):
                time.sleep(1)
                
                # Make prediction
                inp_data = [[total_sqft, bath, bhk, encoded_loc]]
                pred = model.predict(inp_data)
                pred_price_cr = float(f"{pred[0]:.2f}")
                pred_price = pred_price_cr * 100000
                
                # Calculate adjustments
                adjustment = calculate_price_adjustment(condition, parking, garden, security, renovation, age)
                final_price = pred_price * adjustment
                price_range_low = final_price * 0.92
                price_range_high = final_price * 1.08
                lakhs, crores = format_price(final_price)
                
                # Display prediction card
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
                            padding: 2.5rem;
                            border-radius: 20px;
                            text-align: center;
                            margin: 2rem 0;
                            box-shadow: 0 15px 35px rgba(0,0,0,0.2);
                            animation: fadeInUp 0.5s ease-out;">
                    <div style="color: rgba(255,255,255,0.9); font-size: 1.2rem; letter-spacing: 1px;">🏆 ESTIMATED PROPERTY VALUE</div>
                    <div style="color: white; font-size: 4rem; font-weight: bold; margin: 0.5rem 0;">
                        ₹ {lakhs:.2f} Lakhs
                    </div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 1.3rem;">₹ {crores:.2f} Crores</div>
                    <div style="color: rgba(255,255,255,0.8); margin-top: 1rem; font-size: 1rem;">
                        📊 Price Range: ₹ {price_range_low/100000:.2f} L - ₹ {price_range_high/100000:.2f} L
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Analysis section
                st.markdown("---")
                st.markdown('<h3 style="text-align: center; color: #2c3e50; font-size: 1.8rem;">📊 Detailed Analysis</h3>', unsafe_allow_html=True)
                
                col1, col2 = st.columns(2, gap="large")
                
                # Price per sqft analysis
                price_per_sqft = final_price / total_sqft
                market_avg_ppsqft = df[col_mapping['price']].sum() / df[col_mapping['area']].sum()
                
                with col1:
                    if price_per_sqft > market_avg_ppsqft:
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6f5 100%);
                                    padding: 1.8rem;
                                    border-radius: 15px;
                                    margin: 0.5rem 0;
                                    border-left: 5px solid #4caf50;">
                            <div style="font-size: 1.3rem; font-weight: bold; color: #2c3e50;">✅ Premium Valuation</div>
                            <div style="font-size: 2.2rem; font-weight: bold; color: #2c3e50; margin: 0.5rem 0;">₹{price_per_sqft:.0f}/sq.ft</div>
                            <div style="color: #5a6c7e; font-size: 1rem;">Above market average by {((price_per_sqft/market_avg_ppsqft)-1)*100:.1f}%</div>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdef5 100%);
                                    padding: 1.8rem;
                                    border-radius: 15px;
                                    margin: 0.5rem 0;
                                    border-left: 5px solid #2196f3;">
                            <div style="font-size: 1.3rem; font-weight: bold; color: #2c3e50;">📉 Good Value</div>
                            <div style="font-size: 2.2rem; font-weight: bold; color: #2c3e50; margin: 0.5rem 0;">₹{price_per_sqft:.0f}/sq.ft</div>
                            <div style="color: #5a6c7e; font-size: 1rem;">Below market average by {(1 - price_per_sqft/market_avg_ppsqft)*100:.1f}%</div>
                        </div>
                        """, unsafe_allow_html=True)
                
                with col2:
                    # ROI potential
                    if price_per_sqft < market_avg_ppsqft * 0.9:
                        roi_color = "#4caf50"
                        roi_text = "High"
                        roi_desc = "Excellent investment opportunity"
                    elif price_per_sqft < market_avg_ppsqft:
                        roi_color = "#ff9800"
                        roi_text = "Moderate"
                        roi_desc = "Good potential for appreciation"
                    else:
                        roi_color = "#2196f3"
                        roi_text = "Standard"
                        roi_desc = "Fair market value"
                    
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
                                padding: 1.8rem;
                                border-radius: 15px;
                                margin: 0.5rem 0;
                                text-align: center;
                                border: 1px solid #ffe0b2;">
                        <div style="font-size: 1.3rem; font-weight: bold; color: #2c3e50;">💹 Investment Potential</div>
                        <div style="font-size: 2.5rem; font-weight: bold; color: {roi_color}; margin: 0.5rem 0;">{roi_text}</div>
                        <div style="color: #5a6c7e; font-size: 1rem;">{roi_desc}</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Additional insights
                st.markdown("---")
                st.markdown('<h3 style="text-align: center; color: #2c3e50; font-size: 1.8rem;">🔍 Additional Insights</h3>', unsafe_allow_html=True)
                
                col3, col4, col5 = st.columns(3, gap="large")
                
                with col3:
                    # Property condition impact
                    condition_values = {"Needs Work": -15, "Average": -5, "Good": 0, "Excellent": 12, "Luxury": 25}
                    impact = condition_values.get(condition, 0)
                    impact_color = "#4caf50" if impact >= 0 else "#f44336"
                    st.markdown(f"""
                    <div style="background: white;
                                padding: 1.2rem;
                                border-radius: 12px;
                                text-align: center;
                                box-shadow: 0 4px 8px rgba(0,0,0,0.05);
                                border: 2px solid #e9ecef;">
                        <div style="font-size: 2rem;">🏠</div>
                        <div style="font-size: 1rem; color: #7f8c8d; margin-top: 0.5rem;">Condition Impact</div>
                        <div style="font-size: 1.8rem; font-weight: bold; color: {impact_color};">{impact:+}%</div>
                        <div style="font-size: 0.9rem; color: #95a5a6;">{condition}</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col4:
                    # Age impact
                    age_impact = -2 * age if age > 20 else (5 if age < 2 else 0)
                    age_color = "#4caf50" if age_impact > 0 else ("#f44336" if age_impact < 0 else "#7f8c8d")
                    st.markdown(f"""
                    <div style="background: white;
                                padding: 1.2rem;
                                border-radius: 12px;
                                text-align: center;
                                box-shadow: 0 4px 8px rgba(0,0,0,0.05);
                                border: 2px solid #e9ecef;">
                        <div style="font-size: 2rem;">📅</div>
                        <div style="font-size: 1rem; color: #7f8c8d; margin-top: 0.5rem;">Age Impact</div>
                        <div style="font-size: 1.8rem; font-weight: bold; color: {age_color};">{age_impact:+}%</div>
                        <div style="font-size: 0.9rem; color: #95a5a6;">{age} years old</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col5:
                    # Amenities count
                    amenities_count = sum([parking, garden, security, renovation])
                    amenities_text = ["None", "Basic", "Good", "Great", "Excellent"][min(amenities_count, 4)]
                    st.markdown(f"""
                    <div style="background: white;
                                padding: 1.2rem;
                                border-radius: 12px;
                                text-align: center;
                                box-shadow: 0 4px 8px rgba(0,0,0,0.05);
                                border: 2px solid #e9ecef;">
                        <div style="font-size: 2rem;">✨</div>
                        <div style="font-size: 1rem; color: #7f8c8d; margin-top: 0.5rem;">Amenities</div>
                        <div style="font-size: 1.8rem; font-weight: bold; color: #3498db;">{amenities_text}</div>
                        <div style="font-size: 0.9rem; color: #95a5a6;">{amenities_count} features</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Recommendation
                st.markdown("---")
                if price_per_sqft < market_avg_ppsqft:
                    st.success("💡 **Recommendation:** This property offers good value for money. Consider investing! 🚀")
                elif price_per_sqft > market_avg_ppsqft * 1.2:
                    st.warning("⚠️ **Note:** This property is priced at a premium. Compare with similar properties in the area.")
                else:
                    st.info("📌 **Market Insight:** This property is priced at market average. Fair value for the location and amenities.")