from django.shortcuts import render
from modelformapp.forms import NewUserForm
# Create your views here.
def index(request):
    return render(request,'modelformapp/index.html')

def users(request):
    form=NewUserForm()
    if request.method=="POST":
        form=NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("Error :Form Invalid")
    return render(request,'modelformapp/user.html',{'form':form})
