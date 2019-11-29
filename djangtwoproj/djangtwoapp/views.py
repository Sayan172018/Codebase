from django.shortcuts import render
from djangtwoapp import models
# Create your views here.
# def index(request):
#     my_dict={'insert_me':'Goto /users to view user information....'}
#     return render(request,'djangtwoapp/user.html',context=my_dict)

def index(request):
    return render(request,'djangtwoapp/user.html')

def user(request):
    user_list=Users.objects.order_by('firstname')
    user_dict={'insert_me':user_list}
    return render(request,'djangtwoapp/user.html',context=user_dict)
