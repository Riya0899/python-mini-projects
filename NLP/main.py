import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

df=pd.read_csv('NLP/train.txt',sep=';',header=None,names=['text','emotion'])
# print(df.head())
# print(df.isnull().sum())
# print(df['emotion'].unique())

######## TEXT PREPROCESSING ###########

# convert to numeric
unique_emotions=df['emotion'].unique()
emotion_numbers={}
i=0
for  emo in unique_emotions:
    emotion_numbers[emo]=i
    i+=1
df['emotion']=df['emotion'].map(emotion_numbers)  
# print(df)   

df['text']=df['text'].apply(lambda x:x.lower())  # lowercasing

# removing punctuation
def remove_punc(txt):
    return txt.translate(str.maketrans('','',string.punctuation))
df['text']=df['text'].apply(remove_punc)

# remove numbers
def remove_numbers(txt):
    new=""
    for i in txt:
        if not i.isdigit():
            new+=i
    return new
df['text']=df['text'].apply(remove_numbers)

# remove emojis - use ascii value

def remove_emoji(txt):
    new=""
    for i in txt:
        if i.isascii():
            new+=i
    return new
df['text']=df['text'].apply(remove_emoji)

# remove stopwords(is,the,was,and)
# nltk.download('punkt_tab')  # library to tokenize the word
# nltk.download('stopwords')

stop_words=set(stopwords.words('english'))
# print(stop_words)

def remove(txt):
    words=word_tokenize(txt)
    cleaned=[]
    for i in words:
        if not i in stop_words:
            cleaned.append(i)
    return ' '.join(cleaned)

df['text']=df['text'].apply(remove)

# print(df.loc[1]['text'])

# from sklearn.model_selection import train_test_split

# X_train, X_test, y_train, y_test = train_test_split(df['text'], df['emotion'], test_size=0.33, random_state=42)

# # coverting into vectors
# from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer

# # using bag of words

# bow_vectorizer=CountVectorizer()

# X_train_bow=bow_vectorizer.fit_transform(X_train)
# X_test_bow=bow_vectorizer.fit_transform(X_test)

# from sklearn.naive_bayes import MultinomialNB
# from sklearn.metrics import accuracy_score

# nb_model=MultinomialNB()
# nb_model.fit(X_train_bow,y_train)

# pred_bow=nb_model.predict(X_test_bow)
# print(accuracy_score(y_test,pred_bow))


# # using tfidf vector

# tfidf_vectorizer=TfidfVectorizer

# X_train_tfidf=tfidf_vectorizer.fit_transform(X_train)
# X_test_tfidf=tfidf_vectorizer.fit_transform(X_test)

# nb2_model=MultinomialNB()
# nb2_model.fit(X_train_bow,y_train)

# y_pred=nb2_model.predict(X_test_tfidf)
# print(accuracy_score(y_test,y_pred))

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['emotion'], test_size=0.33, random_state=42
)

# converting into vectors
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# ✅ Bag of Words

bow_vectorizer = CountVectorizer()

X_train_bow = bow_vectorizer.fit_transform(X_train)
X_test_bow = bow_vectorizer.transform(X_test)  

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

nb_model = MultinomialNB()
nb_model.fit(X_train_bow, y_train)

pred_bow = nb_model.predict(X_test_bow)
print("BOW Accuracy:", accuracy_score(y_test, pred_bow))


# ✅ TF-IDF

tfidf_vectorizer = TfidfVectorizer()   

X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)   

nb2_model = MultinomialNB()
nb2_model.fit(X_train_tfidf, y_train)   

y_pred = nb2_model.predict(X_test_tfidf)
print("TF-IDF Accuracy:", accuracy_score(y_test, y_pred))
