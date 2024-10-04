from . import views
from django.urls import path

urlpatterns=[
    # path('login',views.adminLogin,name='login'),
    path('home',views.adminHome,name='home'),
    path('logout',views.adminLogout,name='logout'),
]