from modules.audio_features import AudioFeatureAnalyzer

analyzer = AudioFeatureAnalyzer()

result = analyzer.analyze_audio("Recording.m4a")

print(result)