
import streamlit as st
import speech_recognition as sr
import tempfile

# =========================================
# VOICE AI
# =========================================

def show_voice_ai():

    st.write("## 🎤 Voice AI")

    st.info(
        "Upload audio and convert speech to text"
    )

    uploaded_audio = st.file_uploader(

        "Upload WAV Audio",

        type=["wav"]
    )

    if uploaded_audio is not None:

        st.audio(uploaded_audio)

        if st.button("🚀 Transcribe Audio"):

            with st.spinner(
                "AI is transcribing..."
            ):

                # SAVE TEMP FILE

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".wav"
                ) as temp_audio:

                    temp_audio.write(
                        uploaded_audio.read()
                    )

                    temp_path = (
                        temp_audio.name
                    )

                recognizer = sr.Recognizer()

                try:

                    with sr.AudioFile(
                        temp_path
                    ) as source:

                        audio_data = (
                            recognizer.record(source)
                        )

                        text = (
                            recognizer.recognize_google(
                                audio_data
                            )
                        )

                    st.success(
                        "✅ Transcription Complete"
                    )

                    st.text_area(

                        "📝 Transcript",

                        text,

                        height=250
                    )

                    # SAVE TO SESSION

                    st.session_state.document_text = text

                except:

                    st.error(
                        "Audio transcription failed."
                    )

