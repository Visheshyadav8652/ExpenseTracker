from django.shortcuts import render
from django.http import HttpResponse

def Income(request):
    return render(request, 'first.html')

# Create your views here.
