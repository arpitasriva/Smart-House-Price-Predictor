import streamlit as st
import plotly.express as px
from utils.data_loader import load_data, get_column_mapping

def render_home():
    """Render home page with enhanced animations"""
    
    # Load data
    df = load_data()
    col_mapping = get_column_mapping()
    
    # Welcome section with better contrast
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 3rem;
                border-radius: 20px;
                text-align: center;
                margin: 1rem 0 2rem 0;
                animation: fadeInUp 0.6s ease-out;">
        <div style="font-size: 4rem; animation: bounce 2s infinite;">🏠✨</div>
        <h2 style="color: white; font-size: 2rem; margin-top: 1rem;">Welcome to Smart Home Price Predictor! 🎉</h2>
        <p style="color: rgba(255,255,255,0.95); font-size: 1.2rem; margin-top: 1rem;">
            Get accurate property valuations powered by advanced machine learning
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key metrics with better contrast
    st.markdown('<div class="section-title">📊 Market Overview</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    avg_price = df[col_mapping['price']].mean() / 100000
    median_price = df[col_mapping['price']].median() / 100000
    total_properties = len(df)
    avg_area = df[col_mapping['area']].mean()
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div>💰</div>
            <div class="metric-value">₹{avg_price:.1f}L</div>
            <div>Average Price</div>
            <div style="color: #4caf50; font-size: 0.9rem;">▲ +12%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div>📊</div>
            <div class="metric-value">₹{median_price:.1f}L</div>
            <div>Median Price</div>
            <div style="color: #7f8c8d; font-size: 0.9rem;">Market Midpoint</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div>🏘️</div>
            <div class="metric-value">{total_properties}</div>
            <div>Total Properties</div>
            <div style="color: #7f8c8d; font-size: 0.9rem;">Active Listings</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div>📐</div>
            <div class="metric-value">{avg_area:.0f}</div>
            <div>Avg Area (sq.ft)</div>
            <div style="color: #7f8c8d; font-size: 0.9rem;">Standard Size</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Features section
    st.markdown('<div class="section-title">✨ Key Features</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    features = [
        {"icon": "🎯", "title": "Accurate Predictions", "desc": "AI-powered estimates with 92% accuracy"},
        {"icon": "📊", "title": "Market Analysis", "desc": "Comprehensive market insights and trends"},
        {"icon": "💡", "title": "Smart Insights", "desc": "ROI predictions and investment opportunities"}
    ]
    
    for col, feature in zip([col1, col2, col3], features):
        with col:
            st.markdown(f"""
            <div class="glass-card" style="text-align: center;">
                <div style="font-size: 3rem; animation: float 3s ease-in-out infinite;">{feature['icon']}</div>
                <h3 style="margin: 15px 0 10px 0;">{feature['title']}</h3>
                <p>{feature['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Market trends
    st.markdown('<div class="section-title">📈 Market Trends Preview</div>', unsafe_allow_html=True)
    
    bhk_price = df.groupby(col_mapping['bhk'])[col_mapping['price']].mean().sort_index() / 100000
    
    fig = px.line(
        x=bhk_price.index,
        y=bhk_price.values,
        title="Average Price Trend by BHK",
        labels={'x': 'BHK', 'y': 'Price (Lakhs ₹)'},
        markers=True
    )
    fig.update_traces(
        line=dict(color='#667eea', width=3),
        marker=dict(size=12, color='#764ba2', symbol='diamond'),
        fill='tozeroy',
        fillcolor='rgba(102, 126, 234, 0.1)'
    )
    fig.update_layout(
        height=450,
        plot_bgcolor='rgba(255,255,255,0.9)',
        paper_bgcolor='rgba(255,255,255,0)',
        title_font_size=20,
        hovermode='x unified',
        font=dict(color='#2c3e50')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Call to action
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Start Predicting Now", use_container_width=True):
            st.query_params["page"] = "predictor"
            st.rerun()