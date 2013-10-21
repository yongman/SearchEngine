import datetime
from django.shortcuts import render
from django.http import HttpResponse
from Website.models import Results
from mymodules.search import dosearch
import sys
from time import clock

PAGE_SIZE=10

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
        #print request.META['SERVER_NAME']+':'+request.META['SERVER_PORT']
        if 'page' in request.GET:
            page = unicode(request.GET['page'])
        else:
            page = unicode(1)
        start = clock()
        
        #this list is used to obtain the total_hits,only total_hits[0] is used.
        total_hits = []
        results = dosearch(q,page,total_hits)
        end = clock()
        return render(request,'res_search.html', {'results' : results,
                                                    'query':q,
                                                    'count':total_hits[0],
                                                    'time':end-start,
                                                    'page':page,
                                                    'total_page':total_hits[0]/PAGE_SIZE,
                                                    'host':request.META['SERVER_NAME'],
                                                    'port':request.META['SERVER_PORT'],
                                                    'nextpage':int(page)+1})
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)
