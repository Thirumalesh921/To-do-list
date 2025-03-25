from django.urls import path
from . import views
import app

urlpatterns = [
    path('',app.views.todo_list,name=''),
    path('accounts/forgot',views.forgot,name='forgot'),
    path('accounts/register',views.register,name='register'),
    path('accounts/login',views.login,name='login'),
    path('accounts/logout',views.logout,name='logout'),
]