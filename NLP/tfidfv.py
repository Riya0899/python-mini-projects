from sklearn.feature_extraction.text import TfidfVectorizer

documents=[
    "I love pizza",
    "Pizza is the best",
    "I love pasta",
    "Pasta is great"
]

vectorizer=TfidfVectorizer()

X=vectorizer.fit_transform(documents)

print("vocabulary",vectorizer.get_feature_names_out())
print("\nBow Matrix:\n",X.toarray())

