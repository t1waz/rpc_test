from django.conf import settings
from django.urls import path

from history import views


urlpatterns = [
    path('scrap/', views.ScrapView.as_view(), name='scrap'),
    path(f'{settings.LOADERIO_TOKEN}/', views.LoaderIOView.as_view(), name='loaderio'),
]
