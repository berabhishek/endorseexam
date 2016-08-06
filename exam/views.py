from django.shortcuts import render

# Create your views here.
def index(request):
	if request.method=='GET':
		return render(request,'index.html',{'ans':None})
	elif request.method=='POST':
		ans = {}
		ans = request.POST
		z = ans['que1']
		return render(request,'index.html',{'ans':z})
