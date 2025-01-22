
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.stock_picker, name="stockpicker"),
    path('stocktracker/', views.stock_tracker, name="stocktracker"),

]
