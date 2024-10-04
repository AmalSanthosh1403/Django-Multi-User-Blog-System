from . import views
from django.urls import path

urlpatterns=[
    path('',views.login,name='login'),
    path('register',views.reg,name='register'),
    path('home',views.home,name='home'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('approval',views.adminapproval,name='approval'),
    path('createpost',views.createpost,name='createpost'),
    path('detailview',views.detailview,name='detailview'),
    path('myblog',views.myblog,name='myblog'),
    path('editmypost/<postidv>',views.editmypost,name='editmypost'),
    path('deletemypost/<postidv>',views.deletemypost,name='deletemypost'),
    path('search',views.search,name='search'),
    path('comment',views.addcomment,name='comment'),
    path('like',views.like,name='like'),
]