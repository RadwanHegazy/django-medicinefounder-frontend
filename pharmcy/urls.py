from django.urls import path
from .views import home, upload

urlpatterns = [
    path('', home.home_view.as_view(), name='home'),
    path('upload/', upload.upload_view.as_view(), name='upload')
]