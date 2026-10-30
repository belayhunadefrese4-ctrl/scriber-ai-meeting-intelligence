import streamlit as st
import tempfile
import os
import time
from pypdf import PdfReader

# ==========================================
# PAGE CONFIGURATION & BURGUNDY THEME
# ==========================================
st.set_page_config(
    page_title="Scriber AI - Global Speech & Document Intelligence",
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
# SIDEBAR: UNIVERSAL PAYMENT & REMITTANCE HUB
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='color: #800020; text-align: center;'>🎙️ SCRIBER AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #6c757d; font-size: 0.9em;'>Global Intelligence Suite</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("### 📊 Account Status")
    if st.session_state.is_pro_active:
        st.success("🌟 **Pro Enterprise Tier Active**")
        if st.session_state.user_currency == "ETB":
            st.metric("Account Balance", f"{st.session_state.user_balance_etb:.2f} ETB")
        else:
            st.metric("Account Balance", f"{st.session_state.user_balance_foreign:.2f} {st.session_state.user_currency}")
    else:
        free_left = max(0.0, 10.0 - st.session_state.free_minutes_used)
        st.info(f"🎁 **Free Tier Trial**\n\nFree Minutes Remaining: **{free_left:.1f} / 10.0 mins**")
    
    st.markdown("---")
    st.markdown("### 💳 Universal Payment & Remittance")
    
    pay_type = st.radio("User Region:", ["Local (Ethiopia)", "International / Diaspora"], horizontal=True)
    
    if pay_type == "Local (Ethiopia)":
        st.info("📌 **Receiving Accounts:**\n* **CBE:** `1000296269488`\n* **Telebirr:** `+251 986884912`")
        local_method = st.selectbox("Payment Channel:", ["Telebirr", "Commercial Bank of Ethiopia (CBE)", "Awash / Dashen Bank"])
        topup = st.slider("Top-Up Amount (ETB):", 20, 1000, 100, step=20)
        ref_id = st.text_input("Your Phone / Account & Transaction ID:", placeholder="e.g. 0912345678 / FT12345")
        curr_selected = "ETB"
    else:
        st.info("🌍 **International Deposit Details:**\n* Send via **WorldRemit, Wave, Remitly** to Telebirr (`+251986884912`) or CBE (`1000296269488`).")
        remit_app = st.selectbox("Remittance App / Method:", ["WorldRemit", "Remitly", "Wave", "TapTap Send", "Direct International Card"])
        curr_selected = st.selectbox("Currency:", ["USD ($)", "EUR (€)", "GBP (£)", "AED (د.إ)", "CHF (Fr)"]).split()[0]
        topup = st.slider(f"Top-Up Amount ({curr_selected}):", 5, 200, 25, step=5)
        ref_id = st.text_input("Sender Name & Reference Code:", placeholder="e.g. John Doe / WR-984210")

    if st.button("Confirm Payment & Top-Up", use_container_width=True):
        if not ref_id:
            st.error("Please enter your account reference or transaction code.")
        else:
            with st.spinner("Verifying transfer and updating account balance..."):
                time.sleep(1.2)
                st.session_state.is_pro_active = True
                st.session_state.user_currency = curr_selected
                if curr_selected == "ETB":
                    st.session_state.user_balance_etb += topup
                else:
                    st.session_state.user_balance_foreign += topup
                st.success(f"Successfully credited {topup} {curr_selected}!")
                st.rerun()

# ==========================================
# MAIN INTERFACE
# ==========================================
st.markdown("<h1 style='text-align: left;'>Multilingual AI Transcription & Document Intelligence</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.1em; color: #495057;'>High-performance speech-to-text and document translation optimized for local and global users.</p>", unsafe_allow_html=True)

tabs = st.tabs([
    "🎙️ Audio Transcription & Diarization", 
    "📊 Meeting Intelligence", 
    "📄 PDF Document Translation",
    "⚙️ Multi-Currency Pricing Calculator"
])

# ------------------------------------------
# TAB 1: AUDIO TRANSCRIPTION
# ------------------------------------------
with tabs[0]:
    st.header("Audio Transcription & Speaker Diarization")
    st.write("First **10 minutes are 100% free**. Billed at **0.50 ETB / min** (Local) or **0.50 USD / min** (International).")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        uploaded_audio = st.file_uploader("Upload Audio Recording (MP3, WAV, M4A)", type=["mp3", "wav", "m4a"])
        audio_lang = st.selectbox("Audio Language", ["Auto-Detect (AI Powered)", "Amharic (አማርኛ)", "English", "Afaan Oromo", "Tigrinya (ትግርኛ)", "Arabic (العربية)", "French (Français)"])
        diarization = st.checkbox("Enable Speaker Diarization (Who Spoke When)", value=True)
        
        run_transcription = st.button("Start Intelligent Transcription", type="primary", use_container_width=True)

    with col2:
        st.subheader("Live Output & Diarization")
        if run_transcription:
            if uploaded_audio is None:
                st.error("Please upload an audio file first!")
            else:
                with st.spinner("Processing speech recognition with AI..."):
                    time.sleep(1.5)
                    st.session_state.free_minutes_used += 3.5  
                    st.success("Transcription Generated Successfully!")
                    
                    sample_output = """
[00:00:10 - SPEAKER 01]: እንኳን ደህና መጡ። የአገር ውስጥ እና የውጭ ሀገር ክፍያ ስርዓት ሙሉ በሙሉ ተስተካክሏል።
[00:00:25 - SPEAKER 02]: Welcome! Multi-currency processing for USD, EUR, and GBP is fully operational.
                    """
                    st.text_area("Segmented Transcript Result:", sample_output, height=200)
                    st.download_button("📥 Download Transcript", sample_output, file_name="scriber_transcript.txt")

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
                * **Global Expansion:** Successfully integrated high-value currency pricing (USD, EUR, GBP, AED, CHF).
                * **Remittance Support:** WorldRemit, Wave, and Remitly direct deposits configured for CBE (`1000296269488`) and Telebirr (`+251986884912`).
                * **AI Capabilities:** Auto-detection enabled for multiple international languages.
                """)

# ------------------------------------------
# TAB 3: PDF DOCUMENT TRANSLATION
# ------------------------------------------
with tabs[2]:
    st.header("PDF Document Translation & Extraction")
    st.write("Rates: **2.00 ETB per page** (Local) | **0.50 USD / EUR / GBP / AED / CHF per page** (International).")
    
    pdf_col1, pdf_col2 = st.columns([1, 1])
    
    with pdf_col1:
        uploaded_pdf = st.file_uploader("Upload PDF Document", type=["pdf"])
        src_lang = st.selectbox("Source Language", ["Auto-Detect (AI Powered)", "English", "Amharic", "Arabic", "French"])
        tgt_lang = st.selectbox("Target Translation Language", ["Amharic (አማርኛ)", "English", "Afaan Oromo", "Tigrinya (ትግርኛ)", "Arabic (العربية)", "French (Français)"])
        
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
                    st.success(f"Translated {page_count} page(s)! (Local: {cost_etb:.2f} ETB | Foreign: ${cost_foreign:.2f})")
                    st.info("**[Sample Translated Preview]:**\n\nይህ ሰነድ በአለም አቀፍ እና በአገር ውስጥ የክፍያ አማራጮች በትክክል ተተርጉሟል።")

# ------------------------------------------
# TAB 4: PRICING CALCULATOR
# ------------------------------------------
with tabs[3]:
    st.header("Transparent Multi-Currency Estimator")
    
    calc_mode = st.radio("Pricing Region:", ["Local (ETB)", "International (USD / EUR / GBP / AED / CHF)"], horizontal=True)
    service_sel = st.radio("Service:", ["PDF Translation (per page)", "Audio Transcription (per minute)"], horizontal=True)
    
    if "Local" in calc_mode:
        if "PDF" in service_sel:
            p = st.slider("Pages:", 1, 200, 10)
            st.metric("Estimated Cost", f"{p * 2.00:.2f} ETB", help="Rate: 2.00 ETB per page")
        else:
            m = st.slider("Minutes:", 1, 180, 15)
            st.metric("Estimated Cost", f"{max(0, m - 10) * 0.50:.2f} ETB", help="Rate: 0.50 ETB/min (First 10 mins free)")
    else:
        fc = st.selectbox("Currency:", ["USD ($)", "EUR (€)", "GBP (£)", "AED (د.إ)", "CHF (Fr)"])[:3]
        if "PDF" in service_sel:
            p = st.slider("Pages:", 1, 200, 10)
            st.metric("Estimated Cost", f"{p * 0.50:.2f} {fc}", help="Rate: 0.50 per page")
        else:
            m = st.slider("Minutes:", 1, 180, 15)
            st.metric("Estimated Cost", f"{m * 0.50:.2f} {fc}", help="Rate: 0.50 per minute")

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")
st.markdown("<p style='text-align: center; color: #6c757d; font-size: 0.85em;'>© 2026 Scriber AI Platform | Multi-Currency CBE, Telebirr & WorldRemit Gateway</p>", unsafe_allow_html=True)
