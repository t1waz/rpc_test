from django.urls import path

from history import views


urlpatterns = [
    path('scrap/', views.ScrapView.as_view(), name='scrap'),
]
