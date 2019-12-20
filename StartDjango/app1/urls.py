from django.urls import path
from . import views as app1_views

app_name ='app1'

urlpatterns = [    
    path('', app1_views.js_test, name="jstest"),
]
