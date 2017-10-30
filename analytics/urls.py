from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	url(r'^well$',views.analyticswells, name = "analyticswells"),
	url(r'^well1$',views.analyticswells1, name = "analyticswells1"),
]