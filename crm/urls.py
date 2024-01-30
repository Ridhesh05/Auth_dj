
from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name=''),

    path('register/',views.register,name='register'),

    path('my-login/',views.my_login,name='my-login'),

    path('dashboard/',views.dashbord,name='dashboard'), 

    path('user_logout/',views.user_logout,name="user-logout"),
]
