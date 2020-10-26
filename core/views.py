from django.shortcuts import render

default_context = {'title': 'OpenMessengerI'}
# Create your views here.
def index(request):
	default_context.update({'title': 'Hello!'})
	return render(request, 'base.html', default_context)
	

