from xml.etree.ElementInclude import include
from django.urls import path, include


urlpatterns = [
    path('', include('url_shortener.urls'))
]
