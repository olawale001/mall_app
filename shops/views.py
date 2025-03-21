from rest_framework import viewsets, permissions
import joblib
import numpy as np
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Shop, Product
from .serializers import ShopSerializer, ProductSerializer


model = joblib.load('ml_models/purchase_recommendation.pkl')
sentiment_model = joblib.load('ml_models/sentiment_model.pkl')
vectorizer = joblib.load('ml_models/vectorizer.pkl')


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['POST'])    
def recommend_product(request):
    customer_id = request.data.get('customer_id')
    purchase_frequency = request.data.get('purchase_frequency')
    price = request.data.get('price')

    input_data = np.array([[customer_id, purchase_frequency, price]])
    recommended_product = model.predict(input_data)[0]
    return Response({'recommended_product_id': recommended_product})

@api_view(['POST'])
def analysis_sentiment(request):
    review = request.data.get('review')
    vectorized_text = vectorizer.transform([review])
    sentiment = sentiment_model.predict(vectorized_text)[0]
    sentiment_label = 'Positive' if sentiment == 1 else 'Negative'
    return Response({'Sentiment': sentiment_label})