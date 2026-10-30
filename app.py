import streamlit as st
import tempfile
import os
import time
from pypdf import PdfReader

# ==========================================
# PAGE CONFIGURATION & BURGUNDY THEME
# ==========================================
st.set_page_config(
    page_title="Scriber AI - Multi-Currency Speech & Document Intelligence",
    page_icon="🎙️",
    layout="wide"
)

st.markdown("""
<style>
    :root {
        --primary-color: #800020; /* Burgundy */
        --background-color: #F8F9FA;
        --secondary-background: #FFFFFF;
        --text-color: #212529;
    }
    .main {
        background-color: var(--background-color);
        color: var(--text-color);
    }
    h1, h2, h3 {
        color: #800020 !important;
        font-family: 'Helvetica Neue', sans-serif;
    }
    div.stButton > button:first-child {
        background-color: #800020;
        color: white;
        border-radius: 6px;
        border: none;
        font-weight: bold;
        padding: 0.5rem 1rem;
    }
    div.stButton > button:first-child:hover {
        background-color: #5c0017;
        color: white;
    }
    section[data-testid="stSidebar"] {
        background-color: #F1F3F5;
        border-right: 1px solid #DEE2E6;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# SESSION STATE & BALANCE
# ==========================================
if "free_minutes_used" not in st.session_state:
    st.session_state.free_minutes_used = 0.0  
if "is_pro_active" not in st.session_state:
    st.session_state.is_pro_active = False
if "user_balance_etb" not in st.session_state:
    st.session_state.user_balance_etb = 0.0
if "user_balance_foreign" not in st.session_state:
    st.session_state.user_balance_foreign = 0.0
if "user_currency" not in st.session_state:
    st.session_state.user_currency = "ETB"

# ==========================================
# SIDEBAR: MULTI-CURRENCY PAYMENT GATEWAY
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='color: #800020; text-align: center;'>🎙️ SCRIBER AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #6c757d; font-size: 0.9em;'>Global Speech & Document Platform</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("### 📊 Account Status")
    if st.session_state.is_pro_active:
        st.success("🌟 **Pro Enterprise Tier Active**")
        if st.session_state.user_currency == "ETB":
            st.metric("Account Credit / Balance", f"{st.session_state.user_balance_etb:.2f} ETB")
        else:
            st.metric("Account Credit / Balance", f"{st.session_state.user_balance_foreign:.2f} {st.session_state.user_currency}")
    else:
        free_left = max(0.0, 10.0 - st.session_state.free_minutes_used)
        st.info(f"🎁 **Free Tier Trial**\n\nFree Minutes Remaining: **{free_left:.1f} / 10.0 mins**")
    
    st.markdown("---")
    st.markdown("### 💳 Universal Payment Gateway")
    
    payment_category = st.radio("Payment Location:", ["Local (Ethiopia)", "International / Diaspora"], horizontal=True)
    
    if payment_category == "Local (Ethiopia)":
        payment_method = st.selectbox("Select Local Option:", [
            "Telebirr Mobile Money", 
            "Commercial Bank of Ethiopia (CBE)", 
            "Other Ethiopian Banks (Awash, Dashen, BOA, Abyssinia)"
        ])
        topup_amount = st.slider("Select Amount (ETB):", min_value=20, max_value=1000, value=100, step=20)
        account_ref = st.text_input("Your Account / Phone Number:", placeholder="e.g. 0912345678")
        selected_curr = "ETB"
    else:
        payment_method = st.selectbox("Select Remittance / Card Option:", [
            "WorldRemit (Direct to CBE / Telebirr)",
            "Remitly / TapTap Send / Wave",
            "International Credit/Debit Card (USD/EUR/GBP/AED/CHF)",
            "PayPal / Stripe Foreign Transfer"
        ])
        selected_curr = st.selectbox("Choose Currency:", ["USD", "EUR", "GBP", "AED", "CHF"])
        topup_amount = st.slider(f"Select Amount ({selected_curr}):", min_value=5, max_value=200, value=25, step=5)
        account_ref = st.text_input("Sender Name / Transaction Ref:", placeholder="e.g. John Doe / WR-984210")

    if st.button("Proceed to Pay & Top Up", use_container_width=True):
        if not account_ref:
            st.error("Please enter your account number or transaction reference.")
        else:
            with st.spinner(f"Connecting to {payment_method}..."):
                time.sleep(1.2)
                st.session_state.is_pro_active = True
                st.session_state.user_currency = selected_curr
                if selected_curr == "ETB":
                    st.session_state.user_balance_etb += topup_amount
                else:
                    st.session_state.user_balance_foreign += topup_amount
                st.success(f"Successfully credited {topup_amount} {selected_curr} via {payment_method}!")
                st.rerun()

# ==========================================
# MAIN INTERFACE
# ==========================================
st.markdown("<h1 style='text-align: left;'>Multilingual AI Transcription & Document Intelligence</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.1em; color: #495057;'>Universal multi-currency speech-to-text and PDF translation platform.</p>", unsafe_allow_html=True)

tabs = st.tabs([
    "🎙️ Audio Transcription & Diarization", 
    "📊 Meeting Intelligence", 
    "📄 PDF Document Translation",
    "⚙️ Usage & Multi-Currency Calculator"
])

# ------------------------------------------
# TAB 1: AUDIO TRANSCRIPTION
# ------------------------------------------
with tabs[0]:
    st.header("Audio Transcription & Speaker Diarization")
    st.write("First **10 minutes are completely free**. Billed at **0.50 ETB / $0.50 USD per minute** after trial.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        uploaded_audio = st.file_uploader("Upload Audio Recording (MP3, WAV, M4A)", type=["mp3", "wav", "m4a"])
        audio_lang = st.selectbox("Audio Language", ["Amharic (አማርኛ)", "English", "Afaan Oromo", "Tigrinya (ትግርኛ)", "Auto-Detect"])
        diarization = st.checkbox("Enable Speaker Diarization", value=True)
        
        run_transcription = st.button("Start Intelligent Transcription", type="primary", use_container_width=True)

    with col2:
        st.subheader("Live Output & Diarization")
        if run_transcription:
            if uploaded_audio is None:
                st.error("Please upload an audio file!")
            else:
                with st.spinner("Processing speech recognition..."):
                    time.sleep(1.5)
                    st.session_state.free_minutes_used += 3.5  
                    st.success("Transcription Generated Successfully!")
                    
                    sample_output = """
[00:00:10 - SPEAKER 01]: እንኳን ደህና መጡ። የዓለም አቀፍ እና የአገር ውስጥ ክፍያ ሲስተም ተስተካክሏል።
[00:00:25 - SPEAKER 02]: WorldRemit, CBE, and Telebirr foreign transfers are all active.
                    """
                    st.text_area("Segmented Transcript Result:", sample_output, height=200)
                    st.download_button("📥 Download Transcript", sample_output, file_name="transcript.txt")

# ------------------------------------------
# TAB 2: MEETING INTELLIGENCE
# ------------------------------------------
with tabs[1]:
    st.header("Meeting Intelligence & Executive Summarizer")
    raw_text = st.text_area("Paste Transcript or Notes:", height=150, placeholder="Paste your meeting notes here...")
    
    if st.button("Generate Executive Summary", type="primary"):
        if not raw_text:
            st.warning("Please enter text to summarize.")
        else:
            with st.spinner("Synthesizing decisions..."):
                time.sleep(1)
                st.markdown("### 📋 Executive Summary Report")
                st.success("""
                * **Global Payment Architecture:** Added support for foreign currencies (USD, EUR, GBP, AED, CHF).
                * **Remittance App Integration:** Enabled WorldRemit, TapTap Send, Wave, and Remitly direct deposits to CBE/Telebirr.
                * **Pricing Standard:** Local rate at 2.00 ETB/page; Foreign rate at 0.50 USD/EUR per page.
                """)

# ------------------------------------------
# TAB 3: PDF DOCUMENT TRANSLATION
# ------------------------------------------
with tabs[2]:
    st.header("PDF Document Translation & Extraction")
    st.write("Rates: **2.00 ETB per page** for local users | **0.50 USD / EUR / GBP / AED / CHF per page** for international users.")
    
    pdf_col1, pdf_col2 = st.columns([1, 1])
    
    with pdf_col1:
        uploaded_pdf = st.file_uploader("Upload PDF Document", type=["pdf"])
        src_lang = st.selectbox("Source Language", ["English", "Amharic", "Auto-Detect"])
        tgt_lang = st.selectbox("Target Language", ["Amharic (አማርኛ)", "English", "Afaan Oromo", "Tigrinya (ትግርኛ)"])
        
        translate_btn = st.button("Translate PDF Now", type="primary", use_container_width=True)

    with pdf_col2:
        st.subheader("Translated Document Output")
        if translate_btn:
            if uploaded_pdf is None:
                st.error("Please upload a PDF document first!")
            else:
                reader = PdfReader(uploaded_pdf)
                page_count = len(reader.pages)
                cost_etb = page_count * 2.00
                cost_foreign = page_count * 0.50
                
                with st.spinner(f"Translating {page_count} pages..."):
                    time.sleep(1.5)
                    st.success(f"Translated {page_count} page(s) successfully! (Local Cost: {cost_etb:.2f} ETB | Foreign Cost: ${cost_foreign:.2f})")
                    st.info("**[Sample Translated Preview]:**\n\nይህ ሰነድ በአለም አቀፍ እና በአገር ውስጥ የክፍያ አማራጮች በትክክል ተተርጉሟል።")

# ------------------------------------------
# TAB 4: PRICING CALCULATOR
# ------------------------------------------
with tabs[3]:
    st.header("Transparent Multi-Currency Estimator")
    
    calc_curr = st.radio("Select Your Billing Currency:", ["ETB (Ethiopia)", "USD / EUR / GBP / AED / CHF (Foreign)"], horizontal=True)
    service_type = st.radio("Select Service:", ["PDF Translation (per page)", "Audio Transcription (per minute)"], horizontal=True)
    
    if "ETB" in calc_curr:
        if "PDF" in service_type:
            pages = st.slider("Number of Pages:", 1, 200, 10)
            st.metric("Estimated Local Cost", f"{pages * 2.00:.2f} ETB", help="Rate: 2.00 ETB per page")
        else:
            mins = st.slider("Audio Minutes:", 1, 180, 15)
            st.metric("Estimated Local Cost", f"{max(0, mins - 10) * 0.50:.2f} ETB", help="Rate: 0.50 ETB per min (First 10 mins free)")
    else:
        curr_symbol = st.selectbox("Foreign Currency Unit:", ["USD ($)", "EUR (€)", "GBP (£)", "AED (د.إ)", "CHF (Fr)"])
        if "PDF" in service_type:
            pages = st.slider("Number of Pages:", 1, 200, 10)
            st.metric("Estimated Foreign Cost", f"{pages * 0.50:.2f} {curr_symbol[:3]}", help="Rate: 0.50 per page")
        else:
            mins = st.slider("Audio Minutes:", 1, 180, 15)
            st.metric("Estimated Foreign Cost", f"{mins * 0.50:.2f} {curr_symbol[:3]}", help="Rate: 0.50 per minute")

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")
st.markdown("<p style='text-align: center; color: #6c757d; font-size: 0.85em;'>© 2026 Scriber AI Platform | Multi-Currency CBE, Telebirr & WorldRemit Gateway</p>", unsafe_allow_html=True)
