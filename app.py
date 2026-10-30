else:
        t_col1, t_col2 = st.columns([1, 1])
        with t_col1:
            p_text = st.text_area("Paste Text to Translate:", height=160, placeholder="Paste your text here...")
            t_src = st.selectbox("Source Language", ["Auto-Detect (Universal)", "English", "Amharic (አማርኛ)", "Afaan Oromo", "Tigrinya (ትግርኛ)", "Arabic", "French", "German", "Spanish"], key="ts")
            t_tgt = st.selectbox("Target Language", ["Amharic (አማርኛ)", "English", "Afaan Oromo", "Tigrinya (ትግርኛ)", "Arabic", "French", "German", "Spanish", "Chinese"], key="tt")
            text_btn = st.button("Translate Pasted Text Universally", type="primary", use_container_width=True)
        with t_col2:
            st.subheader("Universal Contextual Translation Result")
            if text_btn:
                if not p_text:
                    st.error("Please paste text to translate!")
                else:
                    if st.session_state.is_admin or st.session_state.is_pro_active or st.session_state.free_pages_used < 2:
                        with st.spinner(f"Translating your text to {t_tgt} in real time..."):
                            if not st.session_state.is_admin:
                                st.session_state.free_pages_used += 1
                            
                            target_code = lang_code_map.get(t_tgt.split()[0], "am")
                            try:
                                # Add a tiny pause to avoid server rate limits
                                time.sleep(0.8)
                                # Translate the entire block at once as a single request
                                real_translated_text = GoogleTranslator(source='auto', target=target_code).translate(p_text)
                            except Exception as e:
                                real_translated_text = f"Translation error: {str(e)}. Please wait a few seconds and try again."
                            
                            translated_result = (
                                f"[LIVE AUTOMATIC TRANSLATION RESULT]\n"
                                f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                                f"🌐 **Target Language:** {t_tgt}\n\n"
                                f"{real_translated_text}"
                            )
                            
                            st.success("Translation Complete!")
                            st.text_area("Result Box:", translated_result, height=280)
                            st.download_button("📥 Download Translation", translated_result, file_name="dynamic_translation.txt")
                    else:
                        st.warning("⚠️ Free trial exhausted. Please top up in the sidebar.")
