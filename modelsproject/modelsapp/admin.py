from django.contrib import admin
from modelsapp.models import AccessRecord,Topic,Webpage


# Register your models here.
admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(Webpage)
