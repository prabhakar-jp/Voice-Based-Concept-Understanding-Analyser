from modules.semantic_analysis import SemanticAnalyzer

analyzer = SemanticAnalyzer()

result = analyzer.evaluate_concept(
    "Python is a high level programming language with simple syntax",
    "Python is a programming language used for software development, AI, and data science"
)

print(result)