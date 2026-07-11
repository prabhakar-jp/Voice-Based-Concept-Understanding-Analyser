from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class SemanticAnalyzer:

    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def calculate_similarity(self, transcript, reference):

        transcript_embedding = self.model.encode(
            [transcript]
        )

        reference_embedding = self.model.encode(
            [reference]
        )

        score = cosine_similarity(
            transcript_embedding,
            reference_embedding
        )[0][0]

        return round(score * 100, 2)


    def evaluate_concept(self, transcript, reference):

        score = self.calculate_similarity(
            transcript,
            reference
        )

        if score >= 80:
            feedback = "Excellent understanding"
        elif score >= 60:
            feedback = "Good understanding"
        elif score >= 40:
            feedback = "Average understanding"
        else:
            feedback = "Needs improvement"

        return {
            "score": score,
            "feedback": feedback
        }