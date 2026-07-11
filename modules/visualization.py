import librosa
import matplotlib.pyplot as plt


class AudioVisualizer:

    def create_waveform(self, audio_path):

        y, sr = librosa.load(
            audio_path,
            sr=None
        )


        fig = plt.figure(
            figsize=(12, 4)
        )


        plt.plot(y)


        plt.title(
            "Audio Waveform"
        )

        plt.xlabel(
            "Samples"
        )

        plt.ylabel(
            "Amplitude"
        )


        plt.tight_layout()


        return fig