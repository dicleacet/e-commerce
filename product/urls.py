from django.urls import path, include
from product.views import LatestProductsList

urlpatterns = [
    path('latest-products/', LatestProductsList.as_view()),
]