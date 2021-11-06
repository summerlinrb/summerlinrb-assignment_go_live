from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]