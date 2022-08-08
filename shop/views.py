from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'home.html')
def AddtoList(req):
    return render(req,'insert.html')    