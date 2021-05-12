from django.urls import path
from .views import RentFormView

urlpatterns = [
    path('rentform', RentFormView.as_view()),
    
]
