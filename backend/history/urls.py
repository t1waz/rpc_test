from django.conf import settings
from django.urls import path

from history import views


urlpatterns = [
    path('scrap/', views.ScrapView.as_view(), name='scrap'),
    path(settings.LOADERIO_URL, views.LoaderIOView.as_view(), name='loaderio'),
]
