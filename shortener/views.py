from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Url
import uuid
# Create your views here.
def index(request):
	return render(request, "shortener/index.html")


def shortit(request):
	# print(request)
	if request.method == "POST":
		d = "Hey there boi"
		link = request.POST["link"]
		uid = str(uuid.uuid4())[:5]

		new_link = Url()
		
		new_link.link = link
		new_link.uuid = uid

		new_link.save()

		return HttpResponse(uid)

def use(request, pk):
	shortened_url = Url.objects.filter(uuid=pk)
	print(shortened_url)
	if shortened_url:
		link = shortened_url[0].link
		return redirect(link)
	else:
		return HttpResponse('<h1 align="center">Link not found</h1>')

