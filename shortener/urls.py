from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('shortit', views.shortit, name="shortit"),
	path('<str:pk>', views.use, name="use"),
]
