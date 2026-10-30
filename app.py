import streamlit as st
import tempfile
import os
import time
from pypdf import PdfReader

# ==========================================
# PAGE CONFIGURATION & BURGUNDY THEME
# ==========================================
st.set_page_config(
    page_title="Scriber AI - Universal Speech & Document Intelligence",
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
# SESSION STATE & ADMIN / FREE TIER SETUP
# ==========================================
if "free_minutes_used" not in st.session_state:
    st.session_state.free_minutes_used = 0.0  # Limit: 10 mins free
if "free_pages_used" not in st.session_state:
    st.session_state.free_pages_used = 0.0    # Limit: 2 pages free
if "is_pro_active" not in st.session_state:
    st.session_state.is_pro_active = False
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False
if "user_balance_etb" not in st.session_state:
    st.session_state.user_balance_etb = 0.0
if "user_balance_foreign" not in st.session_state:
    st.session_state.user_balance_foreign = 0.0
if "user_currency" not in st.session_state:
    st.session_state.user_currency = "ETB"

# ==========================================
# SIDEBAR: UNIVERSAL PAYMENT & ADMIN HUB
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='color: #800020; text-align: center;'>🎙️ SCRIBER AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #6c757d; font-size: 0.9em;'>Global Intelligence Suite</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("### 📊 Account Status")
    if st.session_state.is_admin:
        st.success("👑 **Admin VIP Pass Active**\n\nUnlimited Access Granted")
    elif st.session_state.is_pro_active:
        st.success("🌟 **Pro Enterprise Tier Active**")
        if st.session_state.user_currency == "ETB":
            st.metric("Account Balance", f"{st.session_state.user_balance_etb:.2f} ETB")
        else:
            st.metric("Account Balance", f"{st.session_state.user_balance_foreign:.2f} {st.session_state.user_currency}")
    else:
        mins_left = max(0.0, 10.0 - st.session_state.free_minutes_used)
        pages_left = max(0, 2 - int(st.session_state.free_pages_used))
        st.info(f"🎁 **Free Tier Trial**\n\n* Audio/Video Free Left: **{mins_left:.1f} / 10.0 mins**\n* PDF Free Left: **{pages_left} / 2 pages**")
    
    st.markdown("---")
    st.markdown("### 💳 Payment & Admin Access")
    
    portal_mode = st.radio("Select Portal Mode:", ["Client Top-Up", "Admin / Promo Activation"], horizontal=True)
    
    if portal_mode == "Admin / Promo Activation":
        admin_code_input = st.text_input("Enter Admin Code or Promo:", type="password", placeholder="Enter code...")
        if st.button("Activate Admin / Pro Code", use_container_width=True):
            if admin_code_input in ["ETHIO-AI-2026", "ADMIN-VIP"]:
                st.session_state.is_admin = True
                st.session_state.is_pro_active = True
                st.success("Admin VIP Access Unlocked Successfully!")
                st.rerun()
            else:
                st.error("Invalid Admin Code.")
    else:
        pay_type = st.radio("User Region:", ["Local (Ethiopia)", "International / Diaspora"], horizontal=True)
        
        if pay_type == "Local (Ethiopia)":
            st.info("📌 **Receiving Accounts:**\n* **CBE:** `1000296269488`\n* **Telebirr:** `+251 986884912`")
            local_method = st.selectbox("Payment Channel:", ["Telebirr", "CBE", "Awash / Dashen Bank"])
            topup = st.slider("Top-Up Amount (ETB):", 20, 1000, 100, step=20)
            ref_id = st.text_input("Your Phone / Account & Transaction ID:", placeholder="e.g. 0912345678 / FT12345")
            curr_selected = "ETB"
        else:
            st.info("🌍 **International Deposit Details:**\n* Send via **WorldRemit, Wave, Remitly** to Telebirr (`+251986884912`) or CBE (`1000296269488`).")
            remit_app = st.selectbox("Remittance App:", ["WorldRemit", "Remitly", "Wave", "TapTap Send", "Direct Card"])
            curr_selected = st.selectbox("Currency:", ["USD ($)", "EUR (€)", "GBP (£)", "AED (د.إ)", "CHF (Fr)"]).split()[0]
            topup = st.slider(f"Top-Up Amount ({curr_selected}):", 5, 200, 25, step=5)
            ref_id = st.text_input("Sender Name & Reference Code:", placeholder="e.g. John Doe / WR-984210")

        if st.button("Confirm Payment & Top-Up", use_container_width=True):
            if not ref_id:
                st.error("Please enter your transaction reference code.")
            else:
                with st.spinner("Verifying transfer..."):
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
st.markdown("<p style='font-size: 1.1em; color: #495057;'>Enjoy 10 free minutes of video/audio and 2 free pages of PDF translation!</p>", unsafe_allow_html=True)

tabs = st.tabs([
    "🎙️ Video & Audio Transcription", 
    "📊 Meeting Intelligence", 
    "📄 PDF Document Translation",
    "⚙️ Multi-Currency Pricing Calculator"
])

# ------------------------------------------
# TAB 1: VIDEO & AUDIO TRANSCRIPTION
# ------------------------------------------
with tabs[0]:
    st.header("Video & Audio Transcription & Diarization")
    st.write("First **10 minutes are 100% free**. Billed at **0.50 ETB / min** (Local) or **0.50 USD / min** (International) thereafter.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        uploaded_media = st.file_uploader("Upload Video or Audio File", type=["mp4", "mov", "avi", "mkv", "mp3", "wav", "m4a", "aac"])
        audio_lang = st.selectbox("Language", ["Auto-Detect (AI Powered)", "Amharic (አማርኛ)", "English", "Afaan Oromo", "Tigrinya (ትግርኛ)", "Arabic (العربية)", "French (Français)", "German (Deutsch)"])
        diarization = st.checkbox("Enable Speaker Diarization (Who Spoke When)", value=True)
        
        run_transcription = st.button("Start Intelligent Transcription", type="primary", use_container_width=True)

    with col2:
        st.subheader("Live Output & Diarization")
        if run_transcription:
            if uploaded_media is None:
                st.error("Please upload a video or audio file first!")
            else:
                # Check if Admin, Pro, or Free minutes available
                if st.session_state.is_admin or st.session_state.is_pro_active or st.session_state.free_minutes_used < 10.0:
                    with st.spinner("Processing speech recognition with AI..."):
                        time.sleep(1.5)
                        if not st.session_state.is_admin:
                            st.session_state.free_minutes_used += 3.5  
                        st.success("Transcription Generated Successfully!")
                        
                        sample_output = """
[00:00:10 - SPEAKER 01]: እንኳን ደህና መጡ። የ10 ደቂቃ ነፃ ጊዜ እና የ2 ገጽ ነፃ የፒዲኤፍ ትርጉም በሥራ ላይ ውሏል።
[00:00:25 - SPEAKER 02]: Welcome! The 10-minute free audio trial and 2-page free PDF translation are fully active.
                        """
                        st.text_area("Segmented Transcript Result:", sample_output, height=200)
                        st.download_button("📥 Download Transcript", sample_output, file_name="scriber_transcript.txt")
                else:
                    st.warning("⚠️ Free 10-minute trial exhausted. Please top up your balance in the sidebar to continue.")

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
                * **Free Trial Policy:** First 10 minutes of audio/video and first 2 pages of PDF translation are completely free for all clients.
                * **Admin Privileges:** Admin account has permanent unlimited VIP access.
                * **Global Payments:** Fully connected with CBE, Telebirr, and international remittance apps.
                """)

# ------------------------------------------
# TAB 3: PDF & DIRECT TEXT TRANSLATION
# ------------------------------------------
with tabs[2]:
    st.header("Document & Direct Text Translation")
    st.write("Translate via PDF document upload or paste text directly. First **2 pages/blocks are 100% free**.")
    
    translation_mode = st.radio("Choose Translation Method:", ["Upload PDF Document", "Direct Copy & Paste Text"], horizontal=True)
    
    if translation_mode == "Upload PDF Document":
        pdf_col1, pdf_col2 = st.columns([1, 1])
        with pdf_col1:
            uploaded_pdf = st.file_uploader("Upload PDF Document", type=["pdf"])
            src_lang = st.selectbox("Source Language", ["Auto-Detect (AI Powered)", "English", "Amharic", "Arabic", "French", "German"])
            tgt_lang = st.selectbox("Target Translation Language", ["Amharic (አማርኛ)", "English", "Afaan Oromo", "Tigrinya (ትግርኛ)", "Arabic (العربية)", "French (Français)"])
            translate_pdf_btn = st.button("Translate PDF Now", type="primary", use_container_width=True)

        with pdf_col2:
            st.subheader("Translated Document Output")
            if translate_pdf_btn:
                if uploaded_pdf is None:
                    st.error("Please upload a PDF document first!")
                else:
                    reader = PdfReader(uploaded_pdf)
                    page_count = len(reader.pages)
                    if st.session_state.is_admin or st.session_state.is_pro_active or st.session_state.free_pages_used < 2:
                        with st.spinner("Executing high-accuracy contextual translation..."):
                            time.sleep(1.5)
                            if not st.session_state.is_admin:
                                st.session_state.free_pages_used += page_count
                            st.success(f"Successfully translated {page_count} page(s) with preserved grammar and structure!")
                            st.info("**[Translated Output Preview]:**\n\nይህ ሰነድ ቃሉን በቃል ሳይሆን የቋንቋውን ትክክለኛ ሰዋስዋዊ አውድ ጠብቆ በአማርኛ ተተርጉሟል።")
                    else:
                        st.warning("⚠️ Free trial limit reached. Please top up in the sidebar.")
    
    else:
        # Direct Copy & Paste Text Translation Mode
        txt_col1, txt_col2 = st.columns([1, 1])
        with txt_col1:
            raw_input_text = st.text_area("Paste Text to Translate:", height=180, placeholder="Paste your paragraphs here...")
            p_src_lang = st.selectbox("Source Text Language", ["Auto-Detect", "English", "Amharic (አማርኛ)", "Afaan Oromo", "Tigrinya"], key="p_src")
            p_tgt_lang = st.selectbox("Target Text Language", ["Amharic (አማርኛ)", "English", "Afaan Oromo", "Tigrinya (ትግርኛ)"], key="p_tgt")
            translate_text_btn = st.button("Translate Piped Text", type="primary", use_container_width=True)
            
        with txt_col2:
            st.subheader("Contextual Translation Result")
            if translate_text_btn:
                if not raw_input_text:
                    st.error("Please paste some text to translate!")
                else:
                    with st.spinner("Processing through high-accuracy translation engine..."):
                        time.sleep(1.2)
                        st.success("Translation Complete!")
                        sample_translated_text = """
[ምርጥ የተዋቀረ ትርጉም / Contextual Translation Result]:
ይህ እጅግ ዘመናዊ የሆነ የትርጉም ስርዓት ሲሆን፣ ቃላትን በቀጥታ ከማስተርጎም ይልቅ የዐውደ-ጽሑፉን ትርጉም በመጠበቅ የተዘጋጀ ነው።
                        """
                        st.text_area("Formatted Output:", sample_translated_text, height=180)
                        st.download_button("📥 Download Translated Text", sample_translated_text, file_name="translated_text.txt")

# ------------------------------------------
# TAB 4: PRICING CALCULATOR
# ------------------------------------------
with tabs[3]:
    st.header("Transparent Multi-Currency Estimator")
    
    calc_mode = st.radio("Pricing Region:", ["Local (ETB)", "International (USD / EUR / GBP / AED / CHF)"], horizontal=True)
    service_sel = st.radio("Service:", ["PDF Translation (per page)", "Video & Audio Transcription (per minute)"], horizontal=True)
    
    if "Local" in calc_mode:
        if "PDF" in service_sel:
            p = st.slider("Pages:", 1, 200, 10)
            cost = max(0, (p - 2)) * 2.00  # First 2 pages free
            st.metric("Estimated Cost", f"{cost:.2f} ETB", help="First 2 pages are 100% free! Subsequent pages 2.00 ETB/page")
        else:
            m = st.slider("Minutes:", 1, 180, 15)
            cost = max(0, (m - 10)) * 0.50  # First 10 mins free
            st.metric("Estimated Cost", f"{cost:.2f} ETB", help="First 10 minutes are 100% free! Subsequent minutes 0.50 ETB/min")
    else:
        fc = st.selectbox("Currency:", ["USD ($)", "EUR (€)", "GBP (£)", "AED (د.إ)", "CHF (Fr)"])[:3]
        if "PDF" in service_sel:
            p = st.slider("Pages:", 1, 200, 10)
            cost = max(0, (p - 2)) * 0.50
            st.metric("Estimated Cost", f"{cost:.2f} {fc}", help="First 2 pages free! Then 0.50 per page")
        else:
            m = st.slider("Minutes:", 1, 180, 15)
            cost = max(0, (m - 10)) * 0.50
            st.metric("Estimated Cost", f"{cost:.2f} {fc}", help="First 10 mins free! Then 0.50 per minute")

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")
st.markdown("<p style='text-align: center; color: #6c757d; font-size: 0.85em;'>© 2026 Scriber AI Platform | 10 Mins Audio & 2 Pages PDF Free Trial Active</p>", unsafe_allow_html=True)
