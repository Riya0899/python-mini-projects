from sklearn.feature_extraction.text import CountVectorizer

documents=[
    "I love pizza",
    "Pizza is the best",
    "I love pasta",
    "Pasta is great"
]

vectorizer=CountVectorizer()

X=vectorizer.fit_transform(documents)

print("vocabulary",vectorizer.get_feature_names_out())
print("\nBow Matrix:\n",X.toarray())

