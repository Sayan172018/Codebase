from django.shortcuts import render
from mtvapp.models import Topic,Webpage,AccessRecord

# Create your views here.
def index(request):
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpages_list}
    return render(request,'mtvapp/index.html',context=date_dict )
