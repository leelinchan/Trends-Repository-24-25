from django.urls import path
from .views import homepage, login_view

urlpatterns = [
    path('', homepage, name='homepage'),
    path('login/', login_view, name='login'),
]
