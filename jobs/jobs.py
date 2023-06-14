"""
from django.conf import settings
import requests
import json
import os



def schedule_api():
	comp_url=url = "https://us-east-1-renderer-read.knack.com/v1/scenes/scene_114/views/view_191/records"
	
	

	payload = ""
	headers = {
	    "cookie": "connect.sid=s^%^3Aj9y-qIEA6KMGLvH6l9PH-qNLP5vgWZNR.2O^%^2FWhC52fsj48b5R5IE^%^2FU8YC0MLwwZKxSG2khMl58Vg",
	    "authority": "us-east-1-renderer-read.knack.com",
	    "accept": "application/json",
	    "accept-language": "en-US,en;q=0.9",
	    "authorization": os.environ['BEARER_TOKEN'],
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
 
	