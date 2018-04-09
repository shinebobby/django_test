from django.urls import path
from . import views


app_name = 'basic_app'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login',views.login,name='user_login'),
]
