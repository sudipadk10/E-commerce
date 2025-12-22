from django.urls import path
from . import views

urlpatterns =[
    path('test/',views.test,name='testpage'),
    path('',views.index , name='index'),
    path('login/',views.login , name='login'),
]