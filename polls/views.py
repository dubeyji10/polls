from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
        now = datetime.datetime.now()
        context = {
            'datetime_now':now
        }
        return render(request,"home.html",context)