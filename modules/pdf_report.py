from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


class PDFReportGenerator:

    def generate_report(
        self,
        filename,
        topic,
        transcript,
        similarity_score,
        audio_features,
        final_score
    ):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        content = []


        content.append(
            Paragraph(
                "Voice-Based Concept Understanding Analyser Report",
                styles["Title"]
            )
        )

        content.append(Spacer(1, 12))


        content.append(
            Paragraph(
                f"Topic: {topic}",
                styles["Normal"]
            )
        )


        content.append(
            Paragraph(
                f"Concept Understanding Score: {similarity_score:.2f}%",
                styles["Normal"]
            )
        )


        content.append(
            Paragraph(
                f"Speech Duration: {audio_features['duration']} seconds",
                styles["Normal"]
            )
        )


        content.append(
            Paragraph(
                f"Voice Energy: {audio_features['rms_energy']}",
                styles["Normal"]
            )
        )


        content.append(
            Paragraph(
                f"Final VBCUA Score: {final_score:.2f}%",
                styles["Normal"]
            )
        )


        content.append(Spacer(1, 12))


        content.append(
            Paragraph(
                "Transcript:",
                styles["Heading2"]
            )
        )


        content.append(
            Paragraph(
                transcript,
                styles["Normal"]
            )
        )


        doc.build(content)