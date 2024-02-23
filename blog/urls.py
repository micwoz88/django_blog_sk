from django.urls import path
from . import views # nasze widoki

urlpatterns = [
    path('', views.post_list, name='post_list'),
]