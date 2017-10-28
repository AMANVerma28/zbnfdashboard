from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import coreapi
import json
from django.http import Http404,HttpRequest

# Create your views here.

#View for Analytics Wells.
#It requests data of just well model as it doesn't need others.
def analyticswells(request):
#    data = coreapi.Client()
#    schema = data.get("http://127.0.0.1:2469/well/well")
#    with open('static/json/analyticswell.json', 'w') as outfile:
#        json.dump(schema, outfile)
#    schema = data.get("http://127.0.0.1:2469/well/yield")
#    with open('static/json/analyticsyield.json', 'w') as outfile:
#        json.dump(schema, outfile)
    return render(request,'analytics/wells.html')