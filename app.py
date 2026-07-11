import streamlit as st
import json

from modules.pdf_report import PDFReportGenerator
from modules.scoring import ScoreCalculator
from modules.transcription import SpeechToText
from modules.semantic_analysis import SemanticAnalyzer
from modules.audio_features import AudioFeatureAnalyzer
from modules.visualization import AudioVisualizer


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="VBCUA - Voice Based Concept Understanding Analyser",
    page_icon="🎤",
    layout="wide"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🎤 Voice-Based Concept Understanding Analyser")

st.write(
    "Upload your voice explanation and convert it into text using AI."
)


# --------------------------------------------------
# Load Models
# --------------------------------------------------

@st.cache_resource
def load_models():

    stt_model = SpeechToText()
    semantic_model = SemanticAnalyzer()
    audio_model = AudioFeatureAnalyzer()
    score_model = ScoreCalculator()
    pdf_model = PDFReportGenerator()
    visual_model = AudioVisualizer()

    return (
        stt_model,
        semantic_model,
        audio_model,
        score_model,
        pdf_model,
        visual_model
    )


(
    stt,
    semantic,
    audio_analyzer,
    scorer,
    pdf_generator,
    visualizer
) = load_models()



# --------------------------------------------------
# Load Reference Concepts
# --------------------------------------------------

try:

    with open(
        "data/reference_concepts.json",
        "r"
    ) as file:

        concepts = json.load(file)


except Exception as e:

    st.error(
        f"Reference file error: {e}"
    )

    st.stop()



# --------------------------------------------------
# Topic Selection
# --------------------------------------------------

selected_topic = st.selectbox(
    "Select Topic",
    list(concepts.keys())
)



# --------------------------------------------------
# Audio Upload
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Audio File",
    type=[
        "wav",
        "mp3",
        "m4a"
    ]
)



# --------------------------------------------------
# Main Processing
# --------------------------------------------------

if uploaded_file is not None:


    st.success(
        "Audio uploaded successfully!"
    )


    # Save audio

    audio_path = "temp_audio.m4a"


    with open(
        audio_path,
        "wb"
    ) as f:

        f.write(
            uploaded_file.getbuffer()
        )



    # --------------------------------------------------
    # Speech To Text
    # --------------------------------------------------

    try:

        with st.spinner(
            "Converting speech to text..."
        ):

            transcript = stt.transcribe_audio(
                audio_path
            )


        st.success(
            "Speech-to-Text completed!"
        )


        st.subheader(
            "📝 Transcript"
        )


        st.write(
            transcript
        )


    except Exception as e:

        st.error(
            f"Speech-to-Text Error: {e}"
        )

        st.stop()



    # --------------------------------------------------
    # Semantic Analysis
    # --------------------------------------------------

    try:

        reference_text = concepts[selected_topic]["reference"]


        with st.spinner(
            "Analysing understanding..."
        ):

            similarity_score = semantic.calculate_similarity(
                transcript,
                reference_text
            )


        st.divider()

        st.subheader(
            "🧠 Semantic Analysis"
        )


        st.metric(
            "Similarity Score",
            f"{similarity_score:.2f}%"
        )


        if similarity_score >= 85:

            st.success(
                "Excellent Understanding"
            )

        elif similarity_score >= 70:

            st.info(
                "Good Understanding"
            )

        elif similarity_score >= 50:

            st.warning(
                "Average Understanding"
            )

        else:

            st.error(
                "Needs Improvement"
            )


    except Exception as e:

        st.error(
            f"Semantic Analysis Error: {e}"
        )

        st.stop()



    # --------------------------------------------------
    # Audio Analysis
    # --------------------------------------------------

    try:

        with st.spinner(
            "Analysing voice features..."
        ):

            features = audio_analyzer.analyze_audio(
                audio_path
            )


        st.divider()

        st.subheader(
            "🎧 Audio Analysis"
        )


        st.metric(
            "Speech Duration",
            f"{features['duration']} seconds"
        )


        st.metric(
            "Voice Energy",
            features["rms_energy"]
        )


    except Exception as e:

        st.error(
            f"Audio Analysis Error: {e}"
        )

        st.stop()



    # --------------------------------------------------
    # Waveform Visualization
    # --------------------------------------------------

    try:

        st.divider()

        st.subheader(
            "📊 Audio Waveform"
        )


        waveform = visualizer.create_waveform(
            audio_path
        )


        st.pyplot(
            waveform,
            clear_figure=True
        )


    except Exception as e:

        st.error(
            f"Visualization Error: {e}"
        )



    # --------------------------------------------------
    # Final Score
    # --------------------------------------------------

    try:

        final_score, audio_score = scorer.calculate_final_score(
            similarity_score,
            features
        )


        st.divider()

        st.subheader(
            "🎯 Final VBCUA Score"
        )


        st.metric(
            "Concept Understanding",
            f"{similarity_score:.2f}%"
        )


        st.metric(
            "Speech Quality",
            f"{audio_score:.2f}%"
        )


        st.metric(
            "Overall Score",
            f"{final_score:.2f}%"
        )


        if final_score >= 85:

            st.success(
                "Excellent Understanding"
            )

        elif final_score >= 70:

            st.info(
                "Good Understanding"
            )

        elif final_score >= 50:

            st.warning(
                "Average Understanding"
            )

        else:

            st.error(
                "Needs Improvement"
            )


    except Exception as e:

        st.error(
            f"Score Calculation Error: {e}"
        )

        st.stop()



    # --------------------------------------------------
    # PDF Report
    # --------------------------------------------------

    try:

        report_file = "VBCUA_Report.pdf"


        pdf_generator.generate_report(
            report_file,
            selected_topic,
            transcript,
            similarity_score,
            features,
            final_score
        )


        with open(
            report_file,
            "rb"
        ) as file:


            st.download_button(
                label="📄 Download PDF Report",
                data=file,
                file_name="VBCUA_Report.pdf",
                mime="application/pdf"
            )


    except Exception as e:

        st.error(
            f"PDF Generation Error: {e}"
        )



# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "VBCUA - AI Powered Voice Understanding Analyzer"
)