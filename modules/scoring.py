class ScoreCalculator:

    def calculate_final_score(
        self,
        semantic_score,
        audio_features
    ):

        # Audio score calculation
        audio_score = 0

        duration = audio_features["duration"]
        energy = audio_features["voice_energy"]


        # Duration scoring
        if duration >= 20:
            audio_score += 50
        elif duration >= 10:
            audio_score += 35
        else:
            audio_score += 20


        # Voice energy scoring
        if energy >= 0.05:
            audio_score += 50
        elif energy >= 0.02:
            audio_score += 35
        else:
            audio_score += 20


        # Final combined score
        final_score = (
            (semantic_score * 0.7)
            +
            (audio_score * 0.3)
        )


        return round(final_score, 2), round(audio_score, 2)