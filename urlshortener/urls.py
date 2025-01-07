from django.urls import path
from . import views


urlpatterns = [
    path('', views.UrlShortenerView.as_view(), name='shortener_view'),
    path('<str:short_url>/', views.RedirectShortUrlView.as_view(), name='redirect_view'),
]
