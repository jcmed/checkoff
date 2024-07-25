from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests


import os



def home(request):
	return render(request, 'home.html', {})

def home2(request):
	return render(request, 'home2.html', {})



def home3(request):
	return render(request, 'home3.html', {})

def active_2(request):
	return render(request, '911.html', {})

def fetch_api_data(request):
    access_token = "913c16230cfb43125cbb7098dd3a9ab9a1e693a1"
    base_api_uri = 'https://access.active911.com/interface/open_api/api/'

    context = {
          'access_token': access_token,
	}
    
    return render(request, 'fetch_api_data.html', context)


def active(request):
    access_token = "7c56462989ad2fd79eebdcf171fbb32142da9f8"
    base_api_uri = 'https://access.active911.com/interface/open_api/api/'

    #context = {
          #'access_token': access_token,
	#}
    #return render(request, 'active.html', context)
    return JsonResponse({'base_api_uri' : agency})



	
	
	