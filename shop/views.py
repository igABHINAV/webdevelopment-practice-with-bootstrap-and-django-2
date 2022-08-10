from http.client import HTTPResponse
import imp
from itertools import product
from django.shortcuts import render,redirect,HttpResponse
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import logout , login , authenticate
import math
# Create your views here.   1234!@#$qwer
def index(req):
    # p=Product.objects.all()
    # n=len(p)
    # if req.user.is_anonymous :
    #     return redirect(req,'insert.html')
    if req.method=="POST":

        Username=req.POST.get('emaill')
        password=req.POST.get('passwordy')
        useri=authenticate(req,username=Username,password=password)
        if useri is not None:
            login(req ,useri)
            params={'name':Username}
            return render(req,'insert.html',params) 

        
    else :
        return render(req,'home.html')        
    
    
    
    
    allprods=[]
    c=Product.objects.values('product_category')
    cat={item['product_category'] for item in c}

    for i in cat :
        prod=Product.objects.filter(product_category=i)
        n=len(prod)
        slides=n//4+math.ceil((n/4)-(n//4))
        allprods.append([prod,range(1,slides),slides])


    # params=[[p,range(n),slides],[p,range(n),slides]]
    ap={'ap':allprods}
    return render(req,'home.html',ap)
def AddtoList(req):
    
    return render(req,'insert.html')    