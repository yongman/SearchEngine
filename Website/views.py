import datetime
from django.shortcuts import render
from django.http import HttpResponse
from Website.models import Results
from mymodules.search import dosearch
import sys
from time import clock

def current_time(request):
	now=datetime.datetime.now()
	return render(request,'my_test.html',{'current_time':now})

def home(request):
    now=datetime.datetime.now()
    return render(request,'do_search.html',{'current_time':now})

def search(request):
    """docstring for search"""
    if 'q' in request.GET:
        q = request.GET['q']
        print q
        if 'page' in request.GET:
            page = unicode(request.GET['page'])
        else:
            page = unicode(1)
        start = clock()
        results = dosearch(q,page)
        end = clock()
        return render(request,'res_search.html', {'results' : results,
                                                    'query':q,
                                                    'count':len(results),
                                                    'time':end-start,
                                                    'page':page,
                                                    'nextpage':int(page)+1})
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)
