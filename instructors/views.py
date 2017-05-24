from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from instructors.models import Instructor
# Create your views here.
def hello(request):
    return render(request, "index.html")

def http(request):
    # print(dir(request))
    print(request.path)
    print(request.GET)
    print(request.POST)
    print(request.META)
    print(request.method)
    response = render(request,"http.html")
    print(dir(response))
    print(response['Content-Type'])
    response['Age'] = 2000
    response.status_code = 404
    return response


def instructors_list(request):
    instructors = Instructor.objects.all()
    return render(request,"instructors.html",{"instructors_list":instructors})
def contact(request):
	return render(request,"contact.html")

def student_list(request):
    return render(request,"student_list.html")

def hello_python(request,some):
	return HttpResponse("Hello Python!!! :"+ some)


def sum_two(request,a,b):
	c = int(a)+ int(b)
	print("Hi!!!")
	print(a,b)
	return HttpResponse("Sum  Two paramtrs " + str(c) )
