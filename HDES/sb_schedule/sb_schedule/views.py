# sb_schedule/views.py
from django.shortcuts import render
import datetime

def index(request):
    context = {'year': datetime.datetime.now().year}
    return render(request, 'index.html', context)
