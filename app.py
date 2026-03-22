import streamlit as st
from components.navbar import render_navbar
from components.footer import render_footer

# Import all pages
from pages.home import render_home
from pages.predictor import render_predictor
from pages.market_analysis import render_market_analysis
from pages.price_distribution import render_price_distribution
from pages.insights import render_insights

# Page configuration
st.set_page_config(
    page_icon="🏠",
    page_title="Smart Home Price Predictor",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Get current page for dynamic background
query_params = st.query_params
current_page = query_params.get("page", "home")

# Page-specific lighter backgrounds with better contrast
page_styles = {
    "home": {
        "bg": "linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%)",
        "secondary": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        "text": "#2c3e50",
        "card_bg": "#ffffff",
        "accent": "#667eea"
    },
    "predictor": {
        "bg": "linear-gradient(135deg, #f0f4ff 0%, #e6f0fa 100%)",
        "secondary": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
        "text": "#1e3c72",
        "card_bg": "#ffffff",
        "accent": "#4facfe"
    },
    "market_analysis": {
        "bg": "linear-gradient(135deg, #fff5e6 0%, #ffe6f0 100%)",
        "secondary": "linear-gradient(135deg, #fa709a 0%, #fee140 100%)",
        "text": "#5d3a1a",
        "card_bg": "#ffffff",
        "accent": "#fa709a"
    },
    "price_distribution": {
        "bg": "linear-gradient(135deg, #e8f5e9 0%, #c8e6f5 100%)",
        "secondary": "linear-gradient(135deg, #30cfd0 0%, #330867 100%)",
        "text": "#1b4d3e",
        "card_bg": "#ffffff",
        "accent": "#30cfd0"
    },
    "insights": {
        "bg": "linear-gradient(135deg, #fef9e6 0%, #ffe6e6 100%)",
        "secondary": "linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)",
        "text": "#8b4513",
        "card_bg": "#ffffff",
        "accent": "#ff9a9e"
    }
}

# Get current page style
current_style = page_styles.get(current_page, page_styles["home"])

# Enhanced CSS with better color handling
st.markdown(f"""
<style>
    /* Global animations */
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(30px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    @keyframes fadeInLeft {{
        from {{
            opacity: 0;
            transform: translateX(-30px);
        }}
        to {{
            opacity: 1;
            transform: translateX(0);
        }}
    }}
    
    @keyframes fadeInRight {{
        from {{
            opacity: 0;
            transform: translateX(30px);
        }}
        to {{
            opacity: 1;
            transform: translateX(0);
        }}
    }}
    
    @keyframes zoomIn {{
        from {{
            opacity: 0;
            transform: scale(0.9);
        }}
        to {{
            opacity: 1;
            transform: scale(1);
        }}
    }}
    
    @keyframes bounce {{
        0%, 100% {{
            transform: translateY(0);
        }}
        50% {{
            transform: translateY(-10px);
        }}
    }}
    
    @keyframes float {{
        0% {{
            transform: translateY(0px);
        }}
        50% {{
            transform: translateY(-10px);
        }}
        100% {{
            transform: translateY(0px);
        }}
    }}
    
    /* Main app background */
    .stApp {{
        background: {current_style['bg']};
        animation: fadeInUp 0.8s ease-out;
    }}
    
    /* Glass morphism cards - Darker text for better contrast */
    .glass-card {{
        background: {current_style['card_bg']};
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        animation: fadeInUp 0.6s ease-out;
        border: 1px solid rgba(0, 0, 0, 0.05);
        color: {current_style['text']};
    }}
    
    .glass-card:hover {{
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
    }}
    
    .glass-card h3, .glass-card h4 {{
        color: {current_style['accent']};
        margin-bottom: 15px;
    }}
    
    .glass-card p, .glass-card li {{
        color: {current_style['text']};
    }}
    
    /* Gradient cards - White text for contrast */
    .gradient-card {{
        background: {current_style['secondary']};
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        transition: all 0.4s ease;
        animation: zoomIn 0.5s ease-out;
        color: white;
    }}
    
    .gradient-card h3, .gradient-card h4 {{
        color: white;
    }}
    
    .gradient-card p {{
        color: rgba(255, 255, 255, 0.95);
    }}
    
    .gradient-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
    }}
    
    /* Metric cards - Light background with dark text */
    .metric-card {{
        background: {current_style['card_bg']};
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        transition: all 0.3s ease;
        animation: fadeInUp 0.5s ease-out;
        border: 1px solid rgba(0, 0, 0, 0.05);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        cursor: pointer;
    }}
    
    .metric-card:hover {{
        transform: translateY(-5px) scale(1.03);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
    }}
    
    .metric-value {{
        font-size: 36px;
        font-weight: bold;
        color: {current_style['accent']};
        margin: 10px 0;
    }}
    
    .metric-card div:first-child {{
        font-size: 2rem;
    }}
    
    .metric-card div:last-child {{
        color: {current_style['text']};
        font-size: 0.9rem;
    }}
    
    /* Stats card - Light background with border accent */
    .stats-card {{
        background: {current_style['card_bg']};
        padding: 15px 20px;
        border-radius: 12px;
        margin: 10px 0;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        animation: fadeInLeft 0.5s ease-out;
        border-left: 4px solid {current_style['accent']};
        color: {current_style['text']};
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }}
    
    .stats-card:hover {{
        transform: translateX(10px);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }}
    
    .stats-card strong {{
        color: {current_style['accent']};
    }}
    
    /* Section title */
    .section-title {{
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        margin: 30px 0 20px 0;
        color: {current_style['text']};
        animation: fadeInUp 0.6s ease-out;
        position: relative;
        display: inline-block;
        width: 100%;
    }}
    
    .section-title::after {{
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 60px;
        height: 3px;
        background: {current_style['accent']};
        border-radius: 3px;
        animation: fadeInLeft 0.8s ease-out;
    }}
    
    /* Main header */
    .main-header {{
        text-align: center;
        padding: 2rem;
        background: {current_style['secondary']};
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        animation: slideDown 0.5s ease-out;
    }}
    
    .main-header h1 {{
        color: white !important;
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }}
    
    .main-header p {{
        color: rgba(255, 255, 255, 0.95) !important;
        font-size: 1.2rem;
    }}
    
    @keyframes slideDown {{
        from {{
            opacity: 0;
            transform: translateY(-20px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    /* Prediction card */
    .prediction-card {{
        background: {current_style['secondary']};
        padding: 40px;
        border-radius: 30px;
        text-align: center;
        margin: 20px 0;
        animation: glow 2s ease-in-out infinite;
        position: relative;
        overflow: hidden;
    }}
    
    .prediction-price {{
        font-size: 56px;
        font-weight: bold;
        color: white;
        margin: 15px 0;
    }}
    
    .prediction-card div:first-child {{
        font-size: 20px;
        color: rgba(255, 255, 255, 0.95);
    }}
    
    /* Button styles */
    .stButton > button {{
        background: {current_style['secondary']};
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        border-radius: 10px;
        transition: all 0.3s ease;
        width: 100%;
    }}
    
    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }}
    
    /* Input field styling */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div {{
        background-color: white;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 8px 12px;
        transition: all 0.3s ease;
    }}
    
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus {{
        border-color: {current_style['accent']};
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.1);
    }}
    
    /* Checkbox styling */
    .stCheckbox {{
        background: white;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
    }}
    
    /* Slider styling */
    .stSlider > div > div > div {{
        background-color: {current_style['accent']};
    }}
    
    /* Floating icon */
    .floating-icon {{
        animation: float 3s ease-in-out infinite;
        display: inline-block;
    }}
    
    /* Shimmer text effect */
    .shimmer-text {{
        background: linear-gradient(90deg, {current_style['accent']}, #764ba2, {current_style['accent']});
        background-size: 200% auto;
        color: transparent;
        -webkit-background-clip: text;
        background-clip: text;
        animation: shimmer 3s linear infinite;
    }}
    
    @keyframes shimmer {{
        0% {{
            background-position: -200% center;
        }}
        100% {{
            background-position: 200% center;
        }}
    }}
    
    @keyframes glow {{
        0% {{
            box-shadow: 0 0 5px rgba(102, 126, 234, 0.2);
        }}
        50% {{
            box-shadow: 0 0 20px rgba(102, 126, 234, 0.5);
        }}
        100% {{
            box-shadow: 0 0 5px rgba(102, 126, 234, 0.2);
        }}
    }}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {{
        width: 10px;
        background: rgba(0, 0, 0, 0.05);
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: {current_style['accent']};
        border-radius: 5px;
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: #764ba2;
    }}
    
    /* Text colors for general content */
    h1, h2, h3, h4, h5, h6 {{
        color: {current_style['text']} !important;
    }}
    
    p, li, span, label {{
        color: {current_style['text']} !important;
    }}
    
    /* Success/Info/Warning boxes */
    .info-box {{
        background: #e8f0fe;
        border-left: 4px solid {current_style['accent']};
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        color: #2c3e50;
    }}
    
    .success-box {{
        background: #e8f5e9;
        border-left: 4px solid #4caf50;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        color: #2c3e50;
    }}
    
    .warning-box {{
        background: #fff3e0;
        border-left: 4px solid #ff9800;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        color: #2c3e50;
    }}
</style>
""", unsafe_allow_html=True)

# Display main header
st.markdown(f"""
<div class="main-header">
    <h1>🏠 Smart Home Price Predictor</h1>
    <p>Your AI-powered assistant for accurate real estate valuations</p>
</div>
""", unsafe_allow_html=True)

# Render navigation bar
render_navbar(current_page)

# Page routing
if current_page == "home":
    render_home()
elif current_page == "predictor":
    render_predictor()
elif current_page == "market_analysis":
    render_market_analysis()
elif current_page == "price_distribution":
    render_price_distribution()
elif current_page == "insights":
    render_insights()
else:
    render_home()

# Render footer
render_footer()