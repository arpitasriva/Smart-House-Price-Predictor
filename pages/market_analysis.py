import streamlit as st
import plotly.express as px
from utils.data_loader import load_data, get_column_mapping

def render_market_analysis():
    """Render market analysis page with enhanced visuals"""
    
    st.markdown("""
    <div style="text-align: center; animation: fadeInUp 0.6s ease-out;">
        <div class="floating-icon" style="font-size: 3rem;">📊</div>
        <h1 class="shimmer-text">Market Analysis</h1>
        <p style="margin-bottom: 2rem;">Comprehensive analysis of the real estate market</p>
    </div>
    """, unsafe_allow_html=True)
    
    df = load_data()
    col_mapping = get_column_mapping()
    
    # Key metrics with animated cards
    col1, col2, col3, col4 = st.columns(4)
    
    avg_price = df[col_mapping['price']].mean() / 100000
    max_price = df[col_mapping['price']].max() / 100000
    min_price = df[col_mapping['price']].min() / 100000
    total_properties = len(df)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size: 2rem;">💰</div>
            <div class="metric-value">₹{avg_price:.1f}L</div>
            <div>Average Price</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size: 2rem;">📈</div>
            <div class="metric-value">₹{max_price:.1f}L</div>
            <div>Maximum Price</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size: 2rem;">📉</div>
            <div class="metric-value">₹{min_price:.1f}L</div>
            <div>Minimum Price</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size: 2rem;">🏘️</div>
            <div class="metric-value">{total_properties}</div>
            <div>Total Properties</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Price by BHK with enhanced chart
    st.markdown('<div class="section-title">💰 Price Analysis by BHK</div>', unsafe_allow_html=True)
    
    bhk_price = df.groupby(col_mapping['bhk'])[col_mapping['price']].mean().sort_index() / 100000
    fig = px.bar(
        x=bhk_price.index, 
        y=bhk_price.values,
        title="Average Price by BHK Configuration",
        labels={'x': 'BHK', 'y': 'Price (Lakhs ₹)'},
        color=bhk_price.values,
        color_continuous_scale='Viridis',
        text=bhk_price.values
    )
    fig.update_traces(
        texttemplate='₹%{text:.1f}L', 
        textposition='outside',
        marker_line_color='white',
        marker_line_width=2,
        opacity=0.9
    )
    fig.update_layout(
        height=450,
        showlegend=False,
        plot_bgcolor='rgba(255,255,255,0.9)',
        title_font_size=20,
        hovermode='x unified',
        transition={'duration': 500}
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Location analysis with horizontal bar chart
    st.markdown('<div class="section-title">📍 Top Locations by Average Price</div>', unsafe_allow_html=True)
    
    location_price = df.groupby(col_mapping['location'])[col_mapping['price']].mean().sort_values(ascending=False).head(10) / 100000
    fig = px.bar(
        x=location_price.values,
        y=location_price.index,
        orientation='h',
        title="Top 10 Most Expensive Locations",
        labels={'x': 'Price (Lakhs ₹)', 'y': 'Location'},
        color=location_price.values,
        color_continuous_scale='Plasma',
        text=location_price.values
    )
    fig.update_traces(
        texttemplate='₹%{text:.1f}L',
        textposition='outside',
        marker_line_color='white',
        marker_line_width=1
    )
    fig.update_layout(
        height=500,
        plot_bgcolor='rgba(255,255,255,0.9)',
        title_font_size=20
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Area vs Price with enhanced scatter plot
    st.markdown('<div class="section-title">📐 Area vs Price Correlation</div>', unsafe_allow_html=True)
    
    fig = px.scatter(
        df,
        x=col_mapping['area'],
        y=df[col_mapping['price']]/100000,
        color=col_mapping['bhk'],
        size=col_mapping['bath'],
        title="Area vs Price Relationship",
        labels={'total_sqft': 'Area (sq.ft)', 'price': 'Price (Lakhs ₹)'},
        opacity=0.7,
        hover_data=[col_mapping['location']]
    )
    fig.update_traces(
        marker=dict(
            line=dict(width=1, color='white')
        )
    )
    fig.update_layout(
        height=500,
        plot_bgcolor='rgba(255,255,255,0.9)',
        title_font_size=20,
        hovermode='closest'
    )
    st.plotly_chart(fig, use_container_width=True)