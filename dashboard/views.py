from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import coreapi
import json
from django.http import Http404,HttpRequest

# Create your views here.
def index(request):
    data = coreapi.Client()
    schema = data.get("http://127.0.0.1:8002/household/")
    with open('static/json/household.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://127.0.0.1:8002/farm/")
    with open('static/json/farm.json', 'w') as outfile:
	    json.dump(schema, outfile)
    schema = data.get("http://127.0.0.1:8002/well/")
    with open('static/json/well.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://127.0.0.1:8002/member/")
    with open('static/json/member.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://127.0.0.1:8002/season/")
    with open('static/json/season.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://127.0.0.1:8002/crop/")
    with open('static/json/crop.json', 'w') as outfile:
        json.dump(schema, outfile)
    return render(request,'dashboard/index.html')

def dash(request):
	return render(request,'dashboard/dashboard1.html')