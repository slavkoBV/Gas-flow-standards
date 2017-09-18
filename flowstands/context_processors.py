# -*- coding: utf-8 -*-

from .util import get_regions

def region_processor(request):
	return {'REGIONS': get_regions(request)}