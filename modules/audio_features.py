import librosa
import numpy as np


class AudioFeatureAnalyzer:

    def analyze_audio(self, audio_path):
        # Load audio
        audio, sample_rate = librosa.load(
            audio_path,
            sr=None
        )

        # Duration
        duration = librosa.get_duration(
            y=audio,
            sr=sample_rate
        )

        # RMS Energy
        rms = librosa.feature.rms(y=audio)
        average_energy = float(np.mean(rms))

        # Speaking rate (placeholder)
        words_per_minute = 0

        result = {
            "duration": round(duration, 2),

            # Keep both names for compatibility
            "rms_energy": round(average_energy, 4),
            "voice_energy": round(average_energy, 4),

            "speaking_rate": words_per_minute
        }

        return result