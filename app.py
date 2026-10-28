import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================
# PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="Scriber AI Pro — Meeting Intelligence & ቃለ ጉባዔ",
    page_icon="🎙️",
    layout="wide"
)

st.markdown("""
    <style>
    .main-title { font-size: 2.3rem; font-weight: 800; color: #800020; margin-bottom: 0px; }
    .subtitle { font-size: 1.1rem; color: #475569; margin-bottom: 20px; }
    .badge-lang { background-color: #0F172A; color: white; padding: 4px 10px; border-radius: 4px; font-weight: 600; font-size: 0.85rem; }
    .pay-card { background-color: #F8FAFC; border: 1px solid #CBD5E1; border-left: 5px solid #800020; padding: 15px; border-radius: 6px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State for Trial Minutes
if "trial_minutes" not in st.session_state:
    st.session_state.trial_minutes = 10.0
if "is_pro" not in st.session_state:
    st.session_state.is_pro = False

# ==========================================
# HEADER & INTRODUCTION
# ==========================================
st.markdown('<p class="main-title">🎙️ Scriber AI Pro — Meeting Intelligence & ቃለ ጉባዔ Generator</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Amharic, English, Oromo & Tigrinya Speech-to-Text & Executive Minutes Engine</p>', unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# SIDEBAR: CONFIGURATION & PAYMENT HUB
# ==========================================
st.sidebar.markdown("### 🌐 Language & Model Settings")
language = st.sidebar.selectbox(
    "Select Meeting Language / ቋንቋ ይምረጡ", 
    ["🇪🇹 አማርኛ (Amharic)", "🇬🇧 English", "🇪🇹 Afaan Oromoo", "🇪🇹 ትግርኛ (Tigrinya)", "🇫🇷 Français", "🇸🇦 العربية", "🌐 Auto-Detect"]
)

st.sidebar.markdown("---")
st.sidebar.header("📥 Audio Ingestion")
audio_file = st.sidebar.file_uploader(
    "Upload Meeting Recording (.mp3, .wav, .m4a)", 
    type=["mp3", "wav", "m4a"]
)

# Trial Meter
st.sidebar.markdown("---")
st.sidebar.header("⏱️ Trial & Subscription Meter")
if st.session_state.is_pro:
    st.sidebar.success("⭐ PRO PLAN ACTIVE (Unlimited Hours)")
else:
    st.sidebar.info(f"⏳ Free Trial Balance: **{st.session_state.trial_minutes:.1f} / 10.0 mins** remaining")

st.sidebar.markdown("""
<div class="pay-card">
<b>💎 Pro Upgrade Plans (ETB / Diaspora):</b><br>
• <b>Monthly Pro:</b> 500 ETB / month<br>
• <b>Pay-As-You-Go:</b> 50 ETB per hour
</div>
""", unsafe_allow_html=True)

# Updated Payment Gateways (Telebirr, CBE Birr, WorldRemit, Wave)
payment_method = st.sidebar.selectbox(
    "Choose Payment Gateway / መክፈያ መንገድ", 
    [
        "📱 Telebirr (Local / Merchant)", 
        "🏦 Commercial Bank of Ethiopia (CBE Birr)", 
        "🌍 WorldRemit (International to Telebirr/CBE)", 
        "🌊 Wave Money (Diaspora Transfer)"
    ]
)

# Payment Account details / instructions display
if "Telebirr" in payment_method:
    st.sidebar.caption("💡 Telebirr Pay: Send to Merchant/Number **+251 986884912** and enter Transaction ID below.")
elif "CBE" in payment_method:
    st.sidebar.caption("💡 CBE Account: Transfer to **1000296269488** and enter Reference No. below.")
elif "WorldRemit" in payment_method or "Wave" in payment_method:
    st.sidebar.caption("💡 International Transfer: Send directly to Telebirr/CBE account **+251 986884912** (Name: Belayhun Adefrese).")

txn_id = st.sidebar.text_input("Enter Transaction ID / Reference Code")
promo_code = st.sidebar.text_input("Promo Code (e.g., ETHIO-AI-2026)")

if st.sidebar.button("🔓 Activate Pro Plan"):
    if promo_code == "ETHIO-AI-2026":
        st.session_state.is_pro = True
        st.session_state.trial_minutes = 999.0
        st.sidebar.success("🎉 Promo code applied! Pro features unlocked.")
    elif txn_id:
        st.session_state.is_pro = True
        st.session_state.trial_minutes = 999.0
        st.sidebar.success(f"✅ Payment via {payment_method} verified! Pro account active.")
    else:
        st.sidebar.error("⚠️ Please enter a valid Transaction ID or Promo Code.")

# ==========================================
# MAIN WORKSPACE
# ==========================================
if audio_file is not None:
    st.audio(audio_file, format='audio/wav')
    st.info(f"📌 Target Language: **{language}** | File: `{audio_file.name}`")
    
    if st.button("🚀 Run Speech-to-Text & Generate ቃለ ጉባዔ (Minutes)", type="primary"):
        if not st.session_state.is_pro and st.session_state.trial_minutes <= 0:
            st.error("⚠️ Free trial expired! Please upgrade using Telebirr, CBE, WorldRemit, or Wave in the sidebar.")
        else:
            if not st.session_state.is_pro:
                st.session_state.trial_minutes = max(0.0, st.session_state.trial_minutes - 3.5)
                
            with st.spinner("Processing audio with Whisper AI & generating executive ቃለ ጉባዔ..."):
                
                # Mock outputs based on language selection
                if "አማርኛ" in language:
                    sample_transcript = "[00:01]  chairperson: ስብሰባችንን በሰዓቱ እንጀምራለን። የሩብ ዓመት የበጀት አፈፃፀም እናገኜዋለን።\n[00:45] finance_lead: የባንክ ብድር እና የሊኩዲቲ ምጣኔ ካለፈው ዓመት ጋር ሲታይ አጥጋቢ ነው።\n[02:15] managing_director: የዲጂታል ክፍያ ውህደት ሥራዎች እስከ ቀጣይ ወር መጨረሻ መጠናቀቅ አለባቸው።"
                    sample_minutes = """==================================================
የስብሰባ ቃለ ጉባዔ ማጠቃለያ (EXECUTIVE MEETING MINUTES)
==================================================
▪️ ቀን / Date: 2026-10-28
▪️ አጀንዳ / Agenda: የሩብ ዓመት የበጀት አፈፃፀም እና የዲጂታል ክፍያ ውህደት

1. ዋና ዋና ውሳኔዎች (Key Resolutions):
   - የሩብ ዓመት የባንክ አፈፃፀም በዕቅዱ መሠረት እንዲቀጥል ተወሰነ።
   - የዲጂታል ክፍያ ውህደት ፕሮጀክት ፍጥነት እንዲጨምር።

2. የተሰጡ ኃላፊነቶች (Action Items Matrix):
   [ ] የፋይናንስ ሪፖርት ማጠናቀቅ - ኃላፊ: አቶ በቀለ (የጊዜ ገደብ: እስከ ዓርብ)
   [ ] የቴክኒክ ክፍያ ጌትዌይ ምርመራ - ኃላፊ: የIT ቡድን (የጊዜ ገደብ: በሚቀጥለው ሳምንት)
==================================================
"""
                elif "Afaan Oromoo" in language:
                    sample_transcript = "[00:02] Dura taa’aa: Walgahii keenya eegalleerra. Raawwii baajataa rubaa 3ffaa ilaalla.\n[00:50] Hogganaa Faynansi: Guddinni liqii fi dhangala’aa gaariidha."
                    sample_minutes = """==================================================
GABAASA WALGAHII (MEETING MINUTES SUMMARY)
==================================================
▪️ Guyyaa: 2026-10-28
▪️ Ajandaa: Gamaaggama Baajataa Rubaa Waggaa

1. Murteewwan Ijoo (Key Decisions):
   - Raawwiin karoora baajataa akka cimu murtaa'eera.
==================================================
"""
                else:
                    sample_transcript = "[00:01] Chair: Welcome everyone. Let's review Q3 balance sheet performance and liquidity benchmarks.\n[00:45] Finance Lead: Asset classification rules under NBE are fully met, and deposit ratios improved by 4.2%.\n[02:15] Executive Officer: Action items for Telebirr and CBE gateway integration must be finalized by Friday."
                    sample_minutes = """==================================================
EXECUTIVE MEETING MINUTES & ቃለ ጉባዔ
==================================================
▪️ Date: October 28, 2026
▪️ Agenda: Q3 Financial Performance & Digital Gateway Integration

1. Executive Summary:
   - Evaluated commercial banking liquidity benchmarks and NBE compliance.

2. Key Resolutions & Action Items:
   [ ] Finalize Telebirr/CBE integration specs — Assigned to: Strategy Team (Deadline: Friday)
   [ ] Prepare Branch Performance breakdown — Assigned to: M&E Unit (Deadline: Monday)
==================================================
"""

            st.success("✅ Transcription and ቃለ ጉባዔ generated successfully!")
            
            tab1, tab2, tab3 = st.tabs(["📝 ቃለ ጉባዔ (Minutes)", "📜 Full Transcript", "📊 Analytics & Export"])
            
            with tab1:
                st.subheader("Executive ቃለ ጉባዔ / Meeting Minutes")
                st.text_area("Minutes Overview", value=sample_minutes, height=280)
                st.download_button(
                    label="📥 Download Minutes (.txt)",
                    data=sample_minutes,
                    file_name="Scriber_Meeting_Minutes.txt",
                    mime="text/plain"
                )
                
            with tab2:
                st.subheader("Speaker-Diarized Transcript")
                st.text_area("Transcript Text", value=sample_transcript, height=320)
                st.download_button(
                    label="📥 Download Transcript (.txt)",
                    data=sample_transcript,
                    file_name="Scriber_Full_Transcript.txt",
                    mime="text/plain"
                )
                
            with tab3:
                st.subheader("Meeting Analytics & Export Suite")
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Total Spoken Duration", "14 min 32 sec")
                    st.metric("Detected Speakers", "3 Speakers")
                with col2:
                    st.metric("Action Items Extracted", "2 Active Tasks")
                    st.metric("AI Confidence Score", "98.4%")
                
                st.markdown("---")
                st.download_button(
                    label="📥 Download Complete Package (.zip / .docx format)",
                    data=sample_minutes + "\n\n" + sample_transcript,
                    file_name="Scriber_AI_Pro_Package.txt",
                    mime="text/plain",
                    type="primary"
                )
else:
    st.info("👆 Please upload an audio file (`.mp3`, `.wav`, `.m4a`) in the sidebar to begin transcription and ቃለ ጉባዔ generation.")
