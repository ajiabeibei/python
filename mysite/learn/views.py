from django.shortcuts import render

from .models import Nerong

# Create your views here.
from django.http import HttpResponse

def home(request):
	return render(request,"learn/home.html")

def index(request,a,b):
	first=str(a)
	return HttpResponse("welcome to django!"+first+b)

def title(request,a):
	nerong = Nerong.objects.order_by("nerong_id")[0:3]
	context={"tle":nerong[a],
	}
	return render(request,"learn/title.html",context)
	
