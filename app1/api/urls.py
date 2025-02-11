from django.urls import path
from . import views
urlpatterns = [
    path('random_password',views.random_password)
]
