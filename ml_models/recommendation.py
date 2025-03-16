import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

data = {
    'customer_id' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'product_id' : [101, 102, 103, 104, 101, 102, 103, 101, 104, 102],
    'purchase_frequency' : [5, 3, 8, 1, 2, 4, 6, 7, 9, 10],
    'price' : [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
}

df = pd.DataFrame(data)

X = df[['customer_id', 'purchase_frequency', 'price']]
y = df['product_id']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, 'ml_models/purchase_recommendation.pkl')

print('Model trained and saved successfully.')