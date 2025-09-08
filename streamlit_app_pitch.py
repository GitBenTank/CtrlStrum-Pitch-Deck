import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

# Page config
st.set_page_config(
    page_title="CtrlStrum + ToneGPT AI - Pitch Deck",
    page_icon="🎸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        color: #00d4ff;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        text-align: center;
        color: #ffffff;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 2rem;
        font-weight: 600;
        color: #00d4ff;
        margin: 2rem 0 1rem 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%);
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #333;
        text-align: center;
        margin: 0.5rem;
    }
    .metric-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #00d4ff;
        margin-bottom: 0.5rem;
    }
    .metric-label {
        font-size: 1rem;
        color: #cccccc;
    }
    .feature-box {
        background: #1a1a1a;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #333;
        margin: 0.5rem 0;
    }
    .strumbot-character {
        background: #1a1a1a;
        border: 2px solid #00d4ff;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        margin: 1rem auto;
        max-width: 300px;
    }
    .strumbot-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .strumbot-name {
        font-size: 1.8rem;
        font-weight: 700;
        color: #00d4ff;
        margin-bottom: 0.5rem;
    }
    .strumbot-tagline {
        font-size: 1rem;
        color: #cccccc;
        font-style: italic;
    }
    .contact-info {
        background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%);
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #333;
        text-align: center;
        margin: 0.5rem;
    }
    .sources {
        background: #1a1a1a;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #333;
        font-size: 0.9rem;
        margin: 1rem 0;
    }
    .stApp {
        background: #0a0a0a;
    }
    .stSidebar {
        background: #1a1a1a;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🎸 Pitch Deck Navigation")
st.sidebar.markdown("---")

# Navigation
pages = [
    "Title Slide",
    "The Problem", 
    "The Solution",
    "Market Opportunity",
    "Technology Innovation",
    "Product Demo",
    "Business Model",
    "Revenue Projections",
    "Path to Growth",
    "Go-to-Market Strategy",
    "StrumBot AI Companion",
    "Competitive Advantage",
    "Team & Vision",
    "Funding Requirements",
    "Call to Action",
    "Contact & Demo"
]

selected_page = st.sidebar.selectbox("Select Slide:", pages)

# Title Slide
if selected_page == "Title Slide":
    st.markdown('<div class="main-header">🎸 CtrlStrum + ToneGPT AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Revolutionizing Guitar Tone Creation with AI</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Founder & CEO**  
        Ben Tankersley  
        CtrlStrum Platform
        """)
    
    with col2:
        st.markdown("""
        **Contact**  
        📧 thetonegpt@gmail.com  
        📱 (256) 595-7155  
        🌐 ctrlstrum.com
        """)
    
    with col3:
        st.markdown("""
        **Social Media**  
        🎥 @CtrlStrum (YouTube)  
        🐦 @CtrlStrum (Twitter)  
        📸 @CtrlStrum (Instagram)  
        🎵 @CtrlStrum (TikTok)
        """)
    
    st.markdown("---")
    st.markdown("### 🚀 Spark Huntsville Generator Program")
    st.markdown("**Pitch Deck • 2024**")

# The Problem
elif selected_page == "The Problem":
    st.markdown('<div class="section-header">🚨 The Problem</div>', unsafe_allow_html=True)
    st.markdown("### Guitarists Waste 70% of Their Time on Tone Creation")
    
    # Stats grid
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">70%</div>
            <div class="metric-label">Time Wasted</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">$2.8B</div>
            <div class="metric-label">Annual Gear Spending</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">50M+</div>
            <div class="metric-label">Guitarists Worldwide</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">Hours</div>
            <div class="metric-label">Daily Setup Time</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Chart
    st.markdown("### Time Distribution Analysis")
    
    # Create bar chart
    fig = go.Figure(data=[
        go.Bar(
            x=['Playing Music', 'Tone Creation'],
            y=[30, 70],
            marker_color=['#00d4ff', '#ff6b35'],
            text=['30%', '70%'],
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title="Creative Time vs Setup Time",
        xaxis_title="Activity",
        yaxis_title="Percentage (%)",
        height=400,
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#0a0a0a',
        font=dict(color='white')
    )
    
    st.plotly_chart(fig, use_container_width=True)

# The Solution
elif selected_page == "The Solution":
    st.markdown('<div class="section-header">💡 The Solution</div>', unsafe_allow_html=True)
    st.markdown("### ToneGPT AI: Real-Time AI-Powered Guitar Tone Generation")
    
    # Demo box
    st.markdown("""
    <div style="text-align: center; margin: 25px 0; padding: 20px; background: #1a1a1a; border-radius: 8px; border: 1px solid #333;">
        <div style="font-size: 1.2rem; color: #ffffff; font-weight: 500;">
            "Give me a Metallica-style metal tone" 
            <span style="color: #00d4ff; font-size: 1.4rem; margin: 0 10px;">→</span>
            Complete FM9 patch in 0.5 seconds
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 Key Features")
        st.markdown("""
        - **Natural Language Processing**: Understands guitar terminology
        - **Real-Time Generation**: Instant tone creation
        - **Hardware Integration**: Direct FM9 export
        - **Artist Accuracy**: Authentic tone recreation
        - **Educational Focus**: Learn while you create
        """)
    
    with col2:
        st.markdown("### 🚀 Unique Value")
        st.markdown("""
        - **First-of-its-kind**: No direct competition
        - **Time Savings**: 70% reduction in setup time
        - **Accessibility**: Democratizes professional tone creation
        - **Community Driven**: Built by guitarists, for guitarists
        - **Educational**: Teaches tone theory and gear knowledge
        """)

# Market Opportunity
elif selected_page == "Market Opportunity":
    st.markdown('<div class="section-header">📈 Market Opportunity</div>', unsafe_allow_html=True)
    st.markdown("### Massive Market with No Direct Competition")
    
    # Stats grid
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">$38.7B</div>
            <div class="metric-label">AI Music Market (2033)</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">25.8%</div>
            <div class="metric-label">CAGR Growth</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">60%</div>
            <div class="metric-label">Musicians Using AI</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">82%</div>
            <div class="metric-label">Can't Distinguish AI</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Market growth chart
    st.markdown("### AI Music Market Growth Projection")
    
    years = [2023, 2028, 2031, 2033]
    values = [3.9, 15.2, 25.1, 38.7]
    
    fig = go.Figure(data=[
        go.Bar(
            x=years,
            y=values,
            marker_color='#00d4ff',
            text=[f'${v}B' for v in values],
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title="Market Growth ($B)",
        xaxis_title="Year",
        yaxis_title="Market Size ($B)",
        height=400,
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#0a0a0a',
        font=dict(color='white')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Sources
    st.markdown("""
    <div class="sources">
        <h4>Sources:</h4>
        <ul>
            <li><a href="https://market.us/report/ai-in-music-market/" target="_blank">Market.us - AI in Music Market Report</a></li>
            <li><a href="https://simplebeen.com/ai-music-statistics/" target="_blank">SimpleBeen - AI Music Statistics</a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Technology Innovation
elif selected_page == "Technology Innovation":
    st.markdown('<div class="section-header">🔬 Technology Innovation</div>', unsafe_allow_html=True)
    st.markdown("### Proprietary AI Architecture for Guitar Tone Generation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🧠 AI Core Technology")
        st.markdown("""
        - **Natural Language Processing**: Advanced NLP for guitar terminology
        - **Parameter Mapping**: AI algorithms for hardware parameter optimization
        - **Real-Time Analysis**: Mathematical modeling for audio quality
        - **Learning System**: Continuous improvement from user feedback
        - **Hardware Integration**: Direct FM9 SYX file generation
        """)
    
    with col2:
        st.markdown("### ⚡ Technical Advantages")
        st.markdown("""
        - **Speed**: 0.5-second generation time
        - **Accuracy**: 95%+ parameter accuracy
        - **Scalability**: Cloud-based architecture
        - **Compatibility**: Works with all major modelers
        - **Future-Proof**: Modular design for expansion
        """)
    
    st.markdown("### 🔒 Intellectual Property")
    st.markdown("""
    - **Proprietary Algorithms**: Custom AI models for tone generation
    - **Patent-Pending**: Core technology protection
    - **Trade Secrets**: Parameter mapping and optimization techniques
    - **Brand Protection**: CtrlStrum and ToneGPT trademarks
    """)

# Product Demo
elif selected_page == "Product Demo":
    st.markdown('<div class="section-header">🎬 Product Demo</div>', unsafe_allow_html=True)
    st.markdown("### See ToneGPT AI in Action")
    
    # Demo placeholder
    st.markdown("""
    <div style="background: #1a1a1a; padding: 2rem; border-radius: 8px; border: 1px solid #333; text-align: center;">
        <h3 style="color: #00d4ff; margin-bottom: 1rem;">🎥 Live Demo Video</h3>
        <p style="color: #cccccc; margin-bottom: 1rem;">Watch ToneGPT AI generate professional guitar tones in real-time</p>
        <div style="background: #2a2a2a; padding: 1rem; border-radius: 4px; border: 2px dashed #555;">
            <p style="color: #888;">[Demo Video Placeholder]</p>
            <p style="color: #888; font-size: 0.9rem;">Live demonstration will be shown during presentation</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 Demo Highlights")
        st.markdown("""
        - **Natural Language Input**: "Give me a Stevie Ray Vaughan blues tone"
        - **Instant Generation**: Complete patch in under 1 second
        - **Parameter Accuracy**: All settings optimized for the style
        - **Export Ready**: Direct FM9 SYX file download
        - **Educational**: Shows why each parameter was chosen
        """)
    
    with col2:
        st.markdown("### 🚀 Try It Yourself")
        st.markdown("""
        - **Beta Access**: Available for early adopters
        - **Free Trial**: 7-day free trial with full features
        - **Community**: Join our Discord for updates
        - **Feedback**: Help shape the future of tone creation
        - **Updates**: Regular feature releases and improvements
        """)

# Business Model
elif selected_page == "Business Model":
    st.markdown('<div class="section-header">💰 Business Model</div>', unsafe_allow_html=True)
    st.markdown("### Multiple Revenue Streams for Sustainable Growth")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-box">
            <h3 style="color: #00d4ff; text-align: center;">70% Primary Revenue</h3>
            <ul>
                <li><strong>SaaS Subscriptions:</strong> $19.99-49.99/month</li>
                <li><strong>Tone Marketplace:</strong> 20% commission</li>
                <li><strong>Educational Licensing:</strong> $10K+/year</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-box">
            <h3 style="color: #00d4ff; text-align: center;">20% Secondary Revenue</h3>
            <ul>
                <li><strong>Hardware Partnerships:</strong> 5-10% commission</li>
                <li><strong>API Licensing:</strong> $0.10 per generation</li>
                <li><strong>Custom Development:</strong> $50K+ per client</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-box">
            <h3 style="color: #00d4ff; text-align: center;">10% Tertiary Revenue</h3>
            <ul>
                <li><strong>Content Monetization:</strong> YouTube, courses</li>
                <li><strong>Merchandise:</strong> CtrlStrum branded gear</li>
                <li><strong>Events & Workshops:</strong> In-person and virtual</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Revenue Projections
elif selected_page == "Revenue Projections":
    st.markdown('<div class="section-header">📊 Revenue Projections</div>', unsafe_allow_html=True)
    st.markdown("### Conservative vs Ambitious Growth Scenarios")
    
    # Revenue projection chart
    years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']
    conservative = [150, 600, 1500, 3000, 5000]
    ambitious = [500, 2500, 8000, 15000, 25000]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=years,
        y=conservative,
        mode='lines+markers',
        name='Conservative',
        line=dict(color='#ff6b35', width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=years,
        y=ambitious,
        mode='lines+markers',
        name='Ambitious',
        line=dict(color='#00d4ff', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title="Revenue Projections ($K)",
        xaxis_title="Year",
        yaxis_title="Revenue ($K)",
        height=500,
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#0a0a0a',
        font=dict(color='white'),
        legend=dict(x=0.02, y=0.98)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 Conservative Scenario")
        st.markdown("""
        - **Year 1:** $150K (500 users)
        - **Year 2:** $600K (2,000 users)
        - **Year 3:** $1.5M (5,000 users)
        - **Year 4:** $3M (10,000 users)
        - **Year 5:** $5M (15,000 users)
        """)
    
    with col2:
        st.markdown("### 🚀 Ambitious Scenario")
        st.markdown("""
        - **Year 1:** $500K (1,500 users)
        - **Year 2:** $2.5M (8,000 users)
        - **Year 3:** $8M (25,000 users)
        - **Year 4:** $15M (50,000 users)
        - **Year 5:** $25M (75,000 users)
        """)

# Path to Growth
elif selected_page == "Path to Growth":
    st.markdown('<div class="section-header">🚀 Path to Growth – Key Drivers by Year</div>', unsafe_allow_html=True)
    
    # Year 1
    st.markdown("### 🚀 Year 1 – Foundation & Validation")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Conservative Goal:** $75K – $150K  
        **Ambitious Goal:** $500K
        """)
    
    with col2:
        st.markdown("""
        **Key Levers:**
        - MVP Launch: SaaS subscriptions at $19.99/mo
        - Marketplace Launch: 20% commission on tone packs
        - Community Content: YouTube, TikTok, blog posts
        """)
    
    st.markdown("**Target Milestone:** 500 – 1,000 paying users by year-end")
    
    st.markdown("---")
    
    # Year 2
    st.markdown("### 🌎 Year 2 – Scale & Partnerships")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Conservative Goal:** $300K – $600K  
        **Ambitious Goal:** $2.5M
        """)
    
    with col2:
        st.markdown("""
        **Key Levers:**
        - Hardware Partnerships: 5-10% commission on hardware sales
        - Educational Licensing: $10K+/year per institution
        - API Licensing: $0.10 per tone generation
        """)
    
    st.markdown("**Target Milestone:** 3,000 – 6,000 paying users")
    
    st.markdown("---")
    
    # Year 3
    st.markdown("### 🏆 Year 3 – Expansion & Industry Leadership")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Conservative Goal:** $750K – $1.5M  
        **Ambitious Goal:** $5M – $8M
        """)
    
    with col2:
        st.markdown("""
        **Key Levers:**
        - International Launch: EU, Asia, Latin America
        - Custom Enterprise Solutions: $50K+/client contracts
        - Marketplace Maturity: 1,000+ tone packs listed
        - Events & Community: Virtual and live workshops
        """)
    
    st.markdown("**Target Milestone:** 15,000 – 20,000 paying users")

# Go-to-Market Strategy
elif selected_page == "Go-to-Market Strategy":
    st.markdown('<div class="section-header">🚀 Go-to-Market Strategy</div>', unsafe_allow_html=True)
    st.markdown("### The 'CtrlStrum' Platform Launch Strategy")
    
    # Phase 1
    st.markdown("### 🎯 Phase 1: Community Foundation (M1-6)")
    st.markdown("**Months 1-6**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Primary Goals:**
        - **CtrlStrum Brand Building:** YouTube tutorials, TikTok shorts, blog content
        - **Beta Community:** 1,000 early adopters from guitar forums and Discord
        - **Content Moat:** "Rig Deep Dive" series, artist spotlights, gear reviews
        """)
    
    with col2:
        st.markdown("""
        **Metrics:**
        - 10K YouTube subscribers
        - 5K TikTok followers
        - 1K beta users
        """)
    
    st.markdown("---")
    
    # Phase 2
    st.markdown("### 🤝 Phase 2: Strategic Partnerships (M7-18)")
    st.markdown("**Months 7-18**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Primary Goals:**
        - **Hardware Partnerships:** Fractal Audio, Line 6, Neural DSP integration deals
        - **Educational Licensing:** Berklee, Musicians Institute, online academies
        - **StrumBot Launch:** AI assistant for personalized tone guidance
        """)
    
    with col2:
        st.markdown("""
        **Metrics:**
        - 3 hardware partners
        - 10 educational licenses
        - 50K active users
        """)
    
    st.markdown("---")
    
    # Phase 3
    st.markdown("### 🌍 Phase 3: Global Expansion (M19-36)")
    st.markdown("**Months 19-36**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Primary Goals:**
        - **International Markets:** EU, Asia, Latin America expansion
        - **Enterprise Solutions:** Custom development for major studios
        - **Platform Maturity:** Full CtrlStrum ecosystem with multiple products
        """)
    
    with col2:
        st.markdown("""
        **Metrics:**
        - 15 hardware/API partners
        - 25 educational licenses globally
        - 100K+ active users
        """)

# StrumBot AI Companion
elif selected_page == "StrumBot AI Companion":
    st.markdown('<div class="section-header">🤖 StrumBot - Your AI Music Companion</div>', unsafe_allow_html=True)
    
    # StrumBot character
    st.markdown("""
    <div class="strumbot-character">
        <div class="strumbot-icon">🎸🤖</div>
        <div class="strumbot-name">StrumBot</div>
        <div class="strumbot-tagline">Your AI Music Companion</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Meet StrumBot - The Paperclip of Guitar Tech")
    st.markdown("StrumBot is your friendly AI assistant that makes guitar technology accessible, educational, and fun. Think Clippy, but for guitarists!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-box">
            <h4 style="color: #00d4ff; text-align: center;">🎯 Auto-Generated Prompts</h4>
            <ul>
                <li>Smart suggestions based on your style</li>
                <li>Learning from your preferences</li>
                <li>Contextual recommendations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-box">
            <h4 style="color: #00d4ff; text-align: center;">📚 Educational Companion</h4>
            <ul>
                <li>Explains why certain pedals were chosen</li>
                <li>Teaches tone theory and gear knowledge</li>
                <li>Interactive learning modules</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-box">
            <h4 style="color: #00d4ff; text-align: center;">🔍 Rig Deep Dives</h4>
            <ul>
                <li>Artist rig analysis and breakdowns</li>
                <li>Historical gear information</li>
                <li>Tour-specific setups</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-box">
            <h4 style="color: #00d4ff; text-align: center;">🎛️ Mixing & Production</h4>
            <ul>
                <li>Mixing advice and techniques</li>
                <li>Production workflow optimization</li>
                <li>Studio setup recommendations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-box">
            <h4 style="color: #00d4ff; text-align: center;">🎤 Live Performance</h4>
            <ul>
                <li>Live sound optimization tips</li>
                <li>Stage setup guidance</li>
                <li>Performance troubleshooting</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-box">
            <h4 style="color: #00d4ff; text-align: center;">🛠️ Technical Support</h4>
            <ul>
                <li>Hardware troubleshooting</li>
                <li>Software integration help</li>
                <li>24/7 AI-powered support</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 🎭 Personality Traits")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("**Cute & Professional**")
    with col2:
        st.markdown("**Knowledgeable**")
    with col3:
        st.markdown("**Encouraging**")
    with col4:
        st.markdown("**Always Helpful**")

# Competitive Advantage
elif selected_page == "Competitive Advantage":
    st.markdown('<div class="section-header">🏆 Competitive Advantage</div>', unsafe_allow_html=True)
    st.markdown("### First-Mover Advantage in AI-Powered Guitar Technology")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🚀 Unique Positioning")
        st.markdown("""
        - **No Direct Competition**: First AI-powered guitar tone generator
        - **Real-Time Generation**: Instant results vs. manual programming
        - **Natural Language**: Understands guitar terminology and context
        - **Hardware Integration**: Direct export to professional modelers
        - **Educational Focus**: Teaches while creating
        """)
    
    with col2:
        st.markdown("### 🛡️ Competitive Moats")
        st.markdown("""
        - **Proprietary AI**: Custom algorithms for guitar tone generation
        - **Community Building**: CtrlStrum brand and following
        - **Data Advantage**: User feedback improves accuracy
        - **Network Effects**: More users = better recommendations
        - **Brand Recognition**: First-mover advantage in market
        """)
    
    st.markdown("### 📊 Market Comparison")
    
    # Comparison table
    comparison_data = {
        'Feature': ['AI-Powered Generation', 'Real-Time Results', 'Natural Language', 'Hardware Integration', 'Educational Content', 'Community Features'],
        'ToneGPT': ['✅', '✅', '✅', '✅', '✅', '✅'],
        'Manual Programming': ['❌', '❌', '❌', '✅', '❌', '❌'],
        'Generic AI Tools': ['⚠️', '⚠️', '⚠️', '❌', '❌', '❌']
    }
    
    df = pd.DataFrame(comparison_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

# Team & Vision
elif selected_page == "Team & Vision":
    st.markdown('<div class="section-header">👨‍💻 Team & Vision</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 👤 Founder Profile")
        st.markdown("""
        **Ben Tankersley - Founder & CEO**
        
        - **Background**: Guitarist, tech entrepreneur, AI enthusiast
        - **Experience**: 10+ years in music technology
        - **Vision**: Democratize professional tone creation
        - **Mission**: Make advanced guitar tech accessible to everyone
        - **Community**: Active in guitar forums and Discord communities
        """)
    
    with col2:
        st.markdown("### 🎯 Company Vision")
        st.markdown("""
        **CtrlStrum Platform Mission:**
        
        To become the go-to platform for music technology education and innovation, starting with ToneGPT AI and expanding to a comprehensive ecosystem of tools, content, and community features that empower musicians at every level.
        """)
    
    st.markdown("### 🌟 Core Values")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🎸 Community First**
        - Built by guitarists, for guitarists
        - Open feedback and collaboration
        - Educational focus over profit
        """)
    
    with col2:
        st.markdown("""
        **🚀 Innovation Driven**
        - Cutting-edge AI technology
        - Continuous improvement
        - Future-focused development
        """)
    
    with col3:
        st.markdown("""
        **🤝 Accessibility**
        - Democratize professional tools
        - Make complex tech simple
        - Support all skill levels
        """)

# Funding Requirements
elif selected_page == "Funding Requirements":
    st.markdown('<div class="section-header">💵 Funding Requirements</div>', unsafe_allow_html=True)
    st.markdown("### Seed Round: $750K for 15% Equity")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💰 Investment Details")
        st.markdown("""
        **Funding Amount:** $750K  
        **Equity Offered:** 15%  
        **Pre-money Valuation:** $4.25M  
        **Post-money Valuation:** $5M
        """)
    
    with col2:
        st.markdown("### 📊 Use of Funds")
        st.markdown("""
        **67% ToneGPT Development ($500K)**
        - AI model refinement and optimization
        - Hardware integration and testing
        - User interface and experience design
        - Beta testing and feedback implementation
        
        **33% CtrlStrum Platform ($250K)**
        - Content creation and marketing
        - Community building and engagement
        - StrumBot AI assistant development
        - Educational content and courses
        """)
    
    st.markdown("### 🎯 Investment Opportunity")
    st.markdown("""
    Join us in revolutionizing guitar technology and building the future of music education. 
    This is more than just an investment in ToneGPT – it's an investment in the CtrlStrum platform 
    and the next generation of music technology innovation.
    """)

# Call to Action
elif selected_page == "Call to Action":
    st.markdown('<div class="section-header">🎯 Call to Action</div>', unsafe_allow_html=True)
    st.markdown("### Join the Music Technology Platform Revolution")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%); padding: 2rem; border-radius: 12px; border: 2px solid #00d4ff; text-align: center; margin: 2rem 0;">
        <h2 style="color: #00d4ff; margin-bottom: 1rem;">Ready to Build the Future of Music Technology?</h2>
        <p style="font-size: 1.2rem; color: #ffffff; margin-bottom: 1.5rem;">
            Be part of the CtrlStrum platform revolution. Invest in the future of guitar technology and music education.
        </p>
        <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
            <div style="background: #00d4ff; color: #000; padding: 1rem 2rem; border-radius: 8px; font-weight: 600;">
                $750K Seed Round
            </div>
            <div style="background: #ff6b35; color: #fff; padding: 1rem 2rem; border-radius: 8px; font-weight: 600;">
                15% Equity
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🚀 Why Invest Now?")
        st.markdown("""
        - **First-Mover Advantage**: No direct competition in AI guitar tech
        - **Proven Technology**: Working prototype with real results
        - **Market Timing**: AI adoption at all-time high
        - **Community Ready**: Engaged audience waiting for launch
        - **Scalable Platform**: Multiple revenue streams and expansion opportunities
        """)
    
    with col2:
        st.markdown("### 📈 Expected Returns")
        st.markdown("""
        - **Year 1**: 3-5x revenue growth
        - **Year 2**: 10-15x revenue growth
        - **Year 3**: 25-50x revenue growth
        - **Exit Strategy**: Strategic acquisition or IPO
        - **Timeline**: 3-5 year investment horizon
        """)

# Contact & Demo
elif selected_page == "Contact & Demo":
    st.markdown('<div class="section-header">📞 Contact & Demo</div>', unsafe_allow_html=True)
    st.markdown("### Ready to Build the Future of Music Technology?")
    
    # Contact grid
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="contact-info">
            <h4>📧 Email</h4>
            <p>thetonegpt@gmail.com</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="contact-info">
            <h4>📱 Phone</h4>
            <p>(256) 595-7155</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="contact-info">
            <h4>🌐 Website</h4>
            <p>ctrlstrum.com</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="contact-info">
            <h4>💼 LinkedIn</h4>
            <p>linkedin.com/in/bentankersley</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Social media
    st.markdown("### 🌐 Social Media")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("**🎥 YouTube**\n@CtrlStrum")
    with col2:
        st.markdown("**🐦 Twitter**\n@CtrlStrum")
    with col3:
        st.markdown("**📸 Instagram**\n@CtrlStrum")
    with col4:
        st.markdown("**🎵 TikTok**\n@CtrlStrum")
    
    st.markdown("---")
    
    st.markdown("### 🎸 About the Founder")
    st.markdown("""
    **Ben Tankersley - Founder & CEO, CtrlStrum Platform**
    
    Guitarist, tech entrepreneur, and AI enthusiast with a vision to democratize professional tone creation. 
    Active in the guitar community and passionate about making advanced technology accessible to musicians at every level.
    """)
    
    st.markdown("### 🚀 Next Steps")
    st.markdown("""
    1. **Schedule a Demo**: See ToneGPT AI in action
    2. **Review Materials**: Detailed business plan and financial projections
    3. **Meet the Team**: Get to know the CtrlStrum vision
    4. **Join the Journey**: Be part of the music technology revolution
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888; font-size: 0.9rem; margin-top: 2rem;">
    <p>CtrlStrum + ToneGPT AI • Spark Huntsville Generator Program • 2024</p>
    <p>Revolutionizing Guitar Tone Creation with AI</p>
</div>
""", unsafe_allow_html=True)
