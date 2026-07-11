# 🎤 Voice-Based Concept Understanding Analyser (VBCUA)

## Project Overview

The Voice-Based Concept Understanding Analyser (VBCUA) is an AI-powered web application that evaluates a user's understanding of a topic through voice explanations.

The application converts speech into text, compares the explanation with a reference answer using Natural Language Processing (NLP), analyses speech characteristics, calculates an overall understanding score, and generates a downloadable PDF report.

---

## Objectives

- Convert speech into text.
- Evaluate conceptual understanding using semantic similarity.
- Analyse speech characteristics such as duration and voice energy.
- Generate an overall performance score.
- Produce a downloadable PDF report.

---

## Features

- 🎤 Audio Upload
- 📝 Speech-to-Text Conversion
- 🧠 Semantic Similarity Analysis
- 🎧 Audio Feature Analysis
- 🎯 Final Score Calculation
- 📊 Audio Waveform Visualization
- 📄 PDF Report Generation

---

## Technologies Used

### Programming Language
- Python

### Framework
- Streamlit

### AI / Machine Learning
- OpenAI Whisper
- Sentence Transformers

### Audio Processing
- Librosa
- NumPy

### Visualization
- Matplotlib

### Report Generation
- ReportLab

---

## Project Workflow

1. User uploads an audio recording.
2. Speech is converted into text.
3. Transcript is compared with a reference concept.
4. Semantic similarity score is calculated.
5. Audio features are analysed.
6. Final VBCUA score is generated.
7. PDF report is created.

---

## Project Structure

```
vbuca/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── reference_concepts.json
│
└── modules/
    ├── transcription.py
    ├── semantic_analysis.py
    ├── audio_features.py
    ├── scoring.py
    ├── visualization.py
    └── pdf_report.py
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
streamlit run app.py
```

---

## Output

The application displays:

- Transcript
- Semantic Similarity Score
- Audio Analysis
- Final VBCUA Score
- Downloadable PDF Report

---

## Future Scope

- Real-time microphone recording
- Multi-language support
- Emotion detection
- Grammar analysis
- Cloud deployment

---

## Author

Prabhakar Chintalapudi