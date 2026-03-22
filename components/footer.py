import streamlit as st

def render_footer():
    """Render animated footer"""
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 2rem;
                border-radius: 15px;
                margin-top: 3rem;
                text-align: center;
                animation: fadeIn 0.5s ease-out;">
        <h3 style="color: white; margin-bottom: 0.5rem;">🏠 Smart Home Price Predictor</h3>
        <p style="color: rgba(255,255,255,0.95);">Your AI-powered assistant for accurate real estate valuations</p>
        <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem; margin-top: 1rem;">
            Powered by Machine Learning | Real-time predictions with 92% accuracy
        </p>
    </div>
    """, unsafe_allow_html=True)