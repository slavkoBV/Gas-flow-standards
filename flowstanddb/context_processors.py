# -*- coding: utf-8 -*-

from django.http import HttpRequest

def flowstand_proc(request):
	return {'PORTAL_URL': request.scheme + '://' + request.get_host()}




