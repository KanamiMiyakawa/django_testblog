from django.shortcuts import render
from django.http import HttpResponse

def top(request):
    return render(request, 'pages/top.html')

# Create your views here.
