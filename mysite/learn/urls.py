from django.urls import path

from . import views

urlpatterns = [
	path("<int:a>/<b>",views.index,name="index"),
	path("",views.home,name="home"),
	path("<int:a>",views.title,name="title"),
]