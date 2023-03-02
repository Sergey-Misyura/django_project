from django.shortcuts import render
from . import ml_predict

def home(request):
    return render(request, 'index.html')

def result(request):
    review = str(request.GET["review"])

    output = ml_predict.prediction_model(review)
    return render(request, 'result.html', {'prediction': output})

