from django.conf.urls import url

from .views import *

urlpatterns = [
	url(r'^$', index),
	url(r'^register/$', register),
	url(r'^login/$', login_user),
	url(r'^logout/$', logout_user),
	url(r'^(?P<question_id>[0-9]{1})/$', individual_question),
	]