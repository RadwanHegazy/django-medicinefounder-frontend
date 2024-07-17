from django.urls import path
from .views import login, register, logout

urlpatterns = [
    path('login/',login.login_view.as_view(),name='login'),
    path('register/',register.register_view.as_view(),name='register'),
    path('logout/',logout.logout_view.as_view(),name='logout'),
]