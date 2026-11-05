import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage
from agent import llm, USER_BUDGET_LIMIT

# 1. Page Setup
st.set_page_config(
    page_title="Cani — Antigravity Payment Safeguard",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Futuristic Antigravity & Glassmorphism CSS Inject
st.markdown("""
<style>
    /* Dark Antigravity Background & Fonts */
    .stApp {
        background: radial-gradient(circle at 50% -20%, #0d1b2a, #02040a, #000000);
        color: #e0e6ed;
    }
    
    /* Floating Antigravity Header */
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #00d2ff 0%, #3a7bd5 50%, #00f2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 10px 20px rgba(0, 210, 255, 0.3);
        margin-bottom: 5px;
        animation: float 4s ease-in-out infinite;
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
        color: #8892b0;
        margin-bottom: 25px;
        letter-spacing: 0.5px;
    }

    /* Floating Animation Keyframes */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-8px); }
        100% { transform: translateY(0px); }
    }

    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(16, 26, 43, 0.6);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(0, 210, 255, 0.15);
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: all 0.3s ease-in-out;
    }
    
    .glass-card:hover {
        border-color: rgba(0, 210, 255, 0.4);
        box-shadow: 0 12px 40px 0 rgba(0, 210, 255, 0.2);
        transform: translateY(-4px);
    }

    /* Antigravity Neon Button */
    div.stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #00d2ff 0%, #3a7bd5 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        border-radius: 12px !important;
        height: 52px !important;
        border: none !important;
        box-shadow: 0 0 15px rgba(0, 210, 255, 0.4) !important;
        transition: all 0.3s ease-in-out !important;
    }
    
    div.stButton > button:hover {
        box-shadow: 0 0 25px rgba(0, 210, 255, 0.8) !important;
        transform: scale(1.02);
    }

    /* Input Field Styling */
    .stTextInput input {
        background-color: rgba(10, 15, 29, 0.8) !important;
        color: #00f2fe !important;
        border: 1px solid rgba(0, 210, 255, 0.2) !important;
        border-radius: 10px !important;
        font-size: 1rem !important;
    }
    
    .stTextInput input:focus {
        border-color: #00d2ff !important;
        box-shadow: 0 0 10px rgba(0, 210, 255, 0.5) !important;
    }

    /* Metric Cards in Sidebar */
    [data-testid="stMetricValue"] {
        font-size: 1.8rem !important;
        color: #00d2ff !important;
        text-shadow: 0 0 10px rgba(0, 210, 255, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Controls & Metrics
with st.sidebar:
    st.markdown("<h2 style='color:#00d2ff;'>🌌 Control Core</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.metric(label="Active Budget Guardrail", value=f"${USER_BUDGET_LIMIT:.2f}")
    st.metric(label="System Status", value="ONLINE ⚡")
    st.metric(label="Network", value="PayPal Sandbox")
    st.metric(label="Engine", value="Groq / Llama 3")
    
    st.markdown("---")
    st.markdown("""
        <div style='font-size: 0.85rem; color: #8892b0;'>
            <b>Cani Protocol:</b> Intercepts unauthorized agent purchases prior to API payload dispatch.
        </div>
    """, unsafe_allow_html=True)

# 4. Main Body UI
st.markdown('<div class="hero-title">Cani — Antigravity Commerce Bot</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Autonomous Purchase Interceptor & Real-Time Payment Safeguard</div>', unsafe_allow_html=True)

# Interactive Test Scenario Cards
st.markdown("### ⚡ Floating Test Scenarios")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="glass-card" style="border-left: 4px solid #00f2fe;">
            <h4 style="color: #00f2fe; margin-top:0;">✅ Safe Transaction Test</h4>
            <p style="color: #a8b2d1; font-size: 0.95rem;">"Buy a wireless gaming mouse for $45.00"</p>
            <span style="color: #00f2fe; font-size: 0.8rem;">Status: Under Budget ($100 Limit)</span>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="glass-card" style="border-left: 4px solid #ff4b4b;">
            <h4 style="color: #ff4b4b; margin-top:0;">🛡️ Safeguard Block Test</h4>
            <p style="color: #a8b2d1; font-size: 0.95rem;">"Buy a 4K Curved Monitor for $299.99"</p>
            <span style="color: #ff4b4b; font-size: 0.8rem;">Status: Violation Trigger (> $100 Limit)</span>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Interactive Prompt Input Form
user_input = st.text_input("Enter natural language order request:", placeholder="e.g. Purchase a mechanical keyboard for $75.00")

if st.button("🚀 Execute Autonomous Order"):
    if not user_input.strip():
        st.warning("⚠️ Please provide a transaction command first.")
    else:
        with st.spinner("🌀 Intercepting intent and evaluating safeguard policies..."):
            try:
                system_instruction = (
                    "You are Cani, an autonomous AI payment agent. "
                    "When a user asks to purchase an item, evaluate whether to call the execute_paypal_checkout tool. "
                    "Always state clearly whether the transaction was approved or blocked."
                )
                messages = [
                    SystemMessage(content=system_instruction),
                    HumanMessage(content=user_input)
                ]
                
                response = llm.invoke(messages)
                
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("### 📊 Antigravity Execution Result")
                
                # Visual output rendering inside glowing glass container
                if hasattr(response, 'tool_calls') and response.tool_calls:
                    st.success("✅ **AI Agent triggered the PayPal Checkout Safeguard Tool!**")
                    st.json(response.tool_calls)
                else:
                    st.info(response.content)

            except Exception as e:
                st.error(f"Execution Error: {str(e)}")