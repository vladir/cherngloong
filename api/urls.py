from django.conf.urls import url

from .views import most_recent


urlpatterns = [
    url(r'ig$', most_recent)
]