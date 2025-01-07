from django.urls import path
from . import views


urlpatterns = [
    path('', views.UrlShortenerView.as_view(), name='shortener_view'),
]
