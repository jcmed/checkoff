from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})

def checkoff(request):
	return render(request, 'checkoff.html', {})