import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','modelsproject.settings')

import django
django.setup()
#fake pop script
import random
from modelsapp.models import Topic,Webpage,AccessRecord
from faker import Faker

fakergen=Faker()
topics=['Search','Social','Marketplace','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the topic or the entry
        top=add_topic()
        #create fake data
        fake_url=fakergen.url()
        fake_date=fakergen.date()
        fake_name=fakergen.company()

        #create webpage entry
        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        #create fake AccessRecord
        acc=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)

if __name__=='__main__':
    print("populating script")
    populate(5)
    print("populating complete")
