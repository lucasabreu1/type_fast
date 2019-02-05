from django.urls import path
from .views import fraseRandom

urlpatterns = [
    path('', fraseRandom)

]
