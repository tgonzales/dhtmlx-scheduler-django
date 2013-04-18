from datetime import date, datetime, timedelta
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .models import *

def eventsXML(request):
    eventList = Event.objects.all()
    return render_to_response('events.xml',
                              {'eventList' : eventList},
                                mimetype="application/xhtml+xml")

@csrf_exempt
def dataprocessor(request):

    responseList = []
    
    if request.method == 'POST':

	command = request.POST['!nativeeditor_status']
	    
	if command == 'inserted':
		e = Event()
		e.start_date = request.POST['start_date']
		e.end_date = request.POST['end_date']
		e.text = request.POST['text']
		e.details = ' '
		e.save()
		response = {'type' : 'insert',
			    'sid': request.POST['id'],
			    'tid' : e.id}

	elif command == 'updated':
		e = Event(pk=request.POST['id'])
		e.start_date = request.POST['start_date']
		e.end_date = request.POST['end_date']
		e.text = request.POST['text']
		e.details = ' '
		e.save()
		response = {'type' : 'update',
			    'sid': e.id,
			    'tid' : e.id}


	elif command == 'deleted':
		 e = Event(pk=request.POST['id'])
		 e.delete()
		 response = {'type' : 'delete',
			    'sid': request.POST['id'],
			    'tid' : '0'}

	else:
		 response = {'type' : 'error',
			    'sid': request.POST['id'],
			    'tid' : '0'}

	responseList.append(response)
            
    return render_to_response('dataprocessor.xml', {"responseList": responseList},
                                    mimetype="application/xhtml+xml")

