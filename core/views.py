from django.shortcuts import render

a = 1
# Create your views here.
def index(request):
	global a

	print(dir(request))
	a += 1
	return render(request, 'base.html', {'title': 'Hello!', 'text': 'privet ' + str(a)})

