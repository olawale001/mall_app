import joblib
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = {
    'review': ['Amazing product', 'Worst service', 'Great quality','Not satisfied', 'Love it', 'Terrible exprience' ],
    'sentiment': [1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
vectorizer = CountVectorizer()
x =vectorizer.fit_transform(df['review'])
model = MultinomialNB()
model.fit(x, df['sentiment'])

joblib.dump(model, 'ml_models/sentiment_model.pkl')
joblib.dump(model, 'ml_models/vectorizer.pkl')
print('Sentiment model trained and saved!')
