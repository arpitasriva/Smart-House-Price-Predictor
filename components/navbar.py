import streamlit as st

def render_navbar(current_page):
    """Render navigation bar using Streamlit buttons"""
    
    # Create columns for navigation buttons
    cols = st.columns(5)
    
    nav_items = [
        {"id": "home", "icon": "🏠", "label": "Home"},
        {"id": "predictor", "icon": "💰", "label": "Price Predictor"},
        {"id": "market_analysis", "icon": "📊", "label": "Market Analysis"},
        {"id": "price_distribution", "icon": "📈", "label": "Price Distribution"},
        {"id": "insights", "icon": "🔍", "label": "Insights"}
    ]
    
    # Custom CSS for navigation buttons
    st.markdown("""
    <style>
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 1rem;
        font-weight: 500;
        border-radius: 10px;
        width: 100%;
        transition: all 0.3s ease;
        font-size: 1rem;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    
    .stButton > button:active {
        transform: translateY(0px);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create buttons in columns
    for i, item in enumerate(nav_items):
        with cols[i]:
            # Check if this is the active page
            is_active = (current_page == item["id"])
            
            # Create button with conditional styling
            button_style = "primary" if is_active else "secondary"
            
            if st.button(
                f"{item['icon']} {item['label']}", 
                key=f"nav_{item['id']}", 
                use_container_width=True,
                type=button_style
            ):
                if not is_active:
                    st.query_params["page"] = item["id"]
                    st.rerun()