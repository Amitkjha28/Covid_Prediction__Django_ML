
from django.urls import path
from covidapp import views

urlpatterns = [
    path('',views.myindex),
    path('result',views.myresult,name='result'),
]
