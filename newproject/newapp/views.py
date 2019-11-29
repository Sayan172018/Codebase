from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("hello world")

def help(request):
    my_dict={'insert':"we are happy to help"}
    return render(request,'help.html',context=my_dict)
