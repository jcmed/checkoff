from django.shortcuts import render, redirect
from.models import Reports
from .forms import ReportsForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
	return render(request, 'home.html', {})

def api(request):
	if 'key' in request.GET:
		pass
	return render(request, 'api.html',{})

def reports(request):
	if request.method=='POST':
		form= ReportsForm(request.POST or None)
		if form.is_valid():
			form.save()
			reports = Reports.objects.all
			messages.success(request, ('Report Has Been Added'))
			return render(request, 'reports.html',{'reports': reports})
	else:
		reports = Reports.objects.all
		return render(request, 'reports.html',{'reports': reports})
def delete(request, reports_id):
	report= Reports.objects.get(pk=reports_id)
	report.delete()
	return redirect('reports')

def edit(request, reports_id):
	if request.method == 'POST':
		reports= Reports.objects.get(pk=reports_id)
		form = ReportsForm(request.POST or None, instance=reports)
		
		if form.is_valid():
			form.save()

			
			return redirect('reports')
		else:
			
			return redirect('reports')

	else:
		report= Reports.objects.get(pk=reports_id)
		return render(request,'edit.html',{'report': report})

def checkoff(request):
	import json
	import requests
	from pandas import DataFrame
	import pandas as pd

	comp_url=url = "https://us-east-1-renderer-read.knack.com/v1/scenes/scene_114/views/view_191/records"
	old_url=url = "https://us-east-1-renderer-read.knack.com/v1/scenes/scene_1461/views/view_2549/records"
	incom_url = "https://us-east-1-renderer-read.knack.com/v1/scenes/scene_114/views/view_2517/records"
	#querystring = {"format":"application/json","is today":"^%^22^%^2C^%"}


	payload = ""
	headers = {
	    "cookie": "connect.sid=s^%^3Aj9y-qIEA6KMGLvH6l9PH-qNLP5vgWZNR.2O^%^2FWhC52fsj48b5R5IE^%^2FU8YC0MLwwZKxSG2khMl58Vg",
	    "authority": "us-east-1-renderer-read.knack.com",
	    "accept": "application/json",
	    "accept-language": "en-US,en;q=0.9",
	    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTQwYzcwNTY5ZjNjNmQ3MzNjYjk4YmU1IiwiYXBwbGljYXRpb25faWQiOiI1M2ViYThlOWFjOWMxM2ExMGNiZGQwMzUiLCJpYXQiOjE2ODI4MjQ0Mzd9.AfQT_oBxIQYV-00fB_XYf6YxEedsBzdZah6Jp1E6qzs",
	    "referer": "https://us-east-1-renderer-read.knack.com/api/xdc.html?xdm_e=https^%^3A^%^2F^%^2Fwww.emstatpro.com&xdm_c=default391&xdm_p=1",
	    "sec-ch-ua": "^\^Chromium^^;v=^\^110^^, ^\^Not",
	    "sec-ch-ua-mobile": "?0",
	    "sec-ch-ua-platform": "^\^Windows^^",
	    "sec-fetch-dest": "empty",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-site": "same-origin",
	    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
	    "x-knack-application-id": "53eba8e9ac9c13a10cbdd035",
	    "x-knack-new-builder": "true",
	    "x-knack-rest-api-key": "renderer-session",
	    "x-requested-with": "XMLHttpRequest"
	}
	####get completed data into DF####
	response = requests.request("GET", comp_url, data=payload, headers=headers)
	api= json.loads(response.content)
	rec= (api["records"])
	j=json.dumps(rec)
	df = DataFrame(rec)
	
	#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTQwYzcwNTY5ZjNjNmQ3MzNjYjk4YmU1IiwiYXBwbGljYXRpb25faWQiOiI1M2ViYThlOWFjOWMxM2ExMGNiZGQwMzUiLCJpYXQiOjE2ODI4MjQ0Mzd9.AfQT_oBxIQYV-00fB_XYf6YxEedsBzdZah6Jp1E6qzs




	###get not completed into DF###
	response = requests.request("GET", old_url, data=payload, headers=headers)
	api= json.loads(response.content)
	rec= (api["records"])
	j=json.dumps(rec)
	df2 = DataFrame(rec)
### combine completed and not completed DF
	df3= pd.concat([df, df2], ignore_index=True)
### Convert time, sort by time and drop duplicates###
	df3['field_3'] = pd.to_datetime(df3['field_3'], infer_datetime_format=True)

	date=df3.sort_values (by='field_3', ascending=False) 
	drop=date.drop_duplicates(['field_4'])
	
### Convert DF to table format for HTML###	
	allData=[]
	for i in range(drop.shape[0]):
		temp=drop.iloc[i]
		allData.append(dict(temp))

	response = requests.request("GET", incom_url, data=payload, headers=headers)
	api= json.loads(response.content)
	rec= (api["records"])
	j= json.dumps(rec)
	df4 = DataFrame(rec)

	records=[]
	for i in range(df4.shape[0]):
		record=df4.iloc[i]
		records.append(dict(record))
			
	#records=df4
	

	reports = Reports.objects.all

	












	content= {
		'allData': allData, 
		'records': records,
		'reports': reports,
		}
	
	
	return render(request, 'checkoff.html', content)

### Today's ####



	
	
	