# -*- coding: utf-8 -*-

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def paginate(objects, size, request, context, var_name='object_list'):
    paginator = Paginator(objects, size)
    page = request.GET.get('page', '1')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)

    ON_EACH_SIDE = 2
    ON_ENDS = 3
    DOT = '...'
    page_num = object_list.number

    if paginator.num_pages <= 5:
        page_range = range(1, paginator.num_pages + 1)
    else:
        page_range = []
        if page_num > (ON_EACH_SIDE + ON_ENDS + 1):
            page_range.extend(range(1, ON_ENDS + 1))
            page_range.append(DOT)
            page_range.extend(range(page_num - ON_EACH_SIDE, page_num + 1))
        else:
            page_range.extend(range(1, page_num + 1))
        if page_num < (paginator.num_pages - ON_EACH_SIDE - ON_ENDS):
            page_range.extend(range(page_num + 1, page_num + ON_EACH_SIDE + 1))
            page_range.append(DOT)
            page_range.extend(range(paginator.num_pages - ON_ENDS + 1, paginator.num_pages + 1))
        else:
            page_range.extend(range(page_num + 1, paginator.num_pages + 1))

    context[var_name] = object_list
    context['is_paginated'] = object_list.has_other_pages()
    context['page_obj'] = object_list
    context['paginator'] = paginator
    context['page_range'] = page_range
    context['DOT'] = DOT

    return context


def get_regions(request):
    """Return list of existing regions"""
    # deferred import of Region model to avoid cycled imports
    from .models import Region

    # get currently selected region
    cur_region = get_current_region(request)

    regions = []
    for region in Region.objects.all().order_by('name'):
        regions.append({
            'id': region.id,
            'name': region.name,
            'selected': cur_region and cur_region.id == region.id and True or False
        })
    return regions


def get_current_region(request):
    """Returns currently selected region or None"""

    # we remember selected region in a cookie
    pk = request.COOKIES.get('current_region')

    if pk:
        from .models import Region
        try:
            region = Region.objects.get(pk=int(pk))
        except Region.DoesNotExist:
            return None
        else:
            return region
    else:
        return None


STRIP_SYMBOLS = ('+', ',', ';')


def search(search_text, object_list, search_params):
    """

    :param search_text: search phrase or word
    :param object_list: queryset
    :param search_params: tuple of 2 fields of object_list ORM-model
    :return: objects that satisfy search parameters
    """

    for char in search_text.strip():
        if char in STRIP_SYMBOLS:
            search_text = search_text.replace(char, ' ')
    words = search_text.split()
    results = {'objects': set()}
    for word in words:
        objects = object_list.filter(Q(**{'{}__icontains'.format(search_params[0]): word}) |
                                     Q(**{'{}__icontains'.format(search_params[1]): word}))
        for obj in objects:
            results['objects'].add(obj)
    results['objects'] = list(results['objects'])
    return results
