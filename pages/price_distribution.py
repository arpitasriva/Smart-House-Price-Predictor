import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.data_loader import load_data, get_column_mapping

def render_price_distribution():
    """Render price distribution page with enhanced visuals"""
    
    st.markdown("""
    <div style="text-align: center; animation: fadeInUp 0.6s ease-out;">
        <div class="floating-icon" style="font-size: 3rem;">📈</div>
        <h1 class="shimmer-text">Price Distribution Analysis</h1>
        <p style="margin-bottom: 2rem;">Visualizing how property prices are distributed across different segments</p>
    </div>
    """, unsafe_allow_html=True)
    
    df = load_data()
    col_mapping = get_column_mapping()
    
    # Histogram and Box Plot with enhanced styling
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.histogram(
            df,
            x=df[col_mapping['price']]/100000,
            nbins=50,
            title="Price Distribution",
            labels={'price': 'Price (Lakhs ₹)', 'count': 'Number of Properties'},
            color_discrete_sequence=['#667eea']
        )
        fig.update_traces(
            marker_line_color='white',
            marker_line_width=1,
            opacity=0.8
        )
        fig.update_layout(
            height=450,
            plot_bgcolor='rgba(255,255,255,0.9)',
            bargap=0.05,
            title_font_size=18
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.box(
            df,
            y=df[col_mapping['price']]/100000,
            title="Price Box Plot - Statistical Overview",
            labels={'price': 'Price (Lakhs ₹)'},
            color_discrete_sequence=['#764ba2']
        )
        fig.update_traces(
            boxmean='sd',
            marker_size=4
        )
        fig.update_layout(
            height=450,
            plot_bgcolor='rgba(255,255,255,0.9)',
            title_font_size=18
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Market segments with enhanced pie chart and stats
    st.markdown('<div class="section-title">🎯 Market Segments</div>', unsafe_allow_html=True)
    
    price_bins = pd.qcut(df[col_mapping['price']], q=4, labels=['Budget', 'Affordable', 'Premium', 'Luxury'])
    price_dist = price_bins.value_counts()
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.pie(
            values=price_dist.values,
            names=price_dist.index,
            title="Market Segment Distribution",
            color_discrete_sequence=px.colors.sequential.Purples_r,
            hole=0.3
        )
        fig.update_traces(
            textposition='inside',
            textinfo='percent+label',
            pull=[0.05, 0, 0, 0],
            marker=dict(line=dict(color='white', width=2))
        )
        fig.update_layout(
            height=450,
            title_font_size=18,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        segment_stats = df.groupby(price_bins)[col_mapping['price']].agg(['count', 'mean', 'min', 'max', 'std']).round(2)
        segment_stats['mean'] = segment_stats['mean'] / 100000
        segment_stats['min'] = segment_stats['min'] / 100000
        segment_stats['max'] = segment_stats['max'] / 100000
        segment_stats['std'] = segment_stats['std'] / 100000
        segment_stats.columns = ['Count', 'Avg Price (L)', 'Min Price (L)', 'Max Price (L)', 'Std Dev (L)']
        
        st.markdown("""
        <div class="glass-card">
            <h3>Segment Statistics</h3>
        </div>
        """, unsafe_allow_html=True)
        st.dataframe(segment_stats, use_container_width=True)
    
    # BHK-wise distribution with violin plot
    st.markdown('<div class="section-title">🏠 BHK-wise Price Distribution</div>', unsafe_allow_html=True)
    
    fig = px.violin(
        df,
        x=col_mapping['bhk'],
        y=df[col_mapping['price']]/100000,
        title="Price Distribution by BHK Configuration",
        labels={'bhk': 'BHK', 'price': 'Price (Lakhs ₹)'},
        box=True,
        points='all',
        color=col_mapping['bhk'],
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig.update_traces(
        box_visible=True,
        meanline_visible=True,
        points='all',
        pointpos=0,
        jitter=0.1,
        marker_size=3
    )
    fig.update_layout(
        height=500,
        plot_bgcolor='rgba(255,255,255,0.9)',
        title_font_size=18,
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)