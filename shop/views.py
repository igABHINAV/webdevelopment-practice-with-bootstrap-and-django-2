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
    
    allprods=[]
    c=Product.objects.values('product_category')
    cat={item['product_category'] for item in c}

    for i in cat :
        prod=Product.objects.filter(product_category=i)
        n=len(prod)
        slides=n//4+math.ceil((n/4)-(n//4))
        allprods.append([prod,range(1,slides),slides])

    # params=[[p,range(n),slides],[p,range(n),slides]]
    # 
    if req.method=="POST":
        if req.POST.get('emaill'):
            Username=req.POST.get('emaill')
            password=req.POST.get('passwordy')
            useri=authenticate(req,username=Username,password=password)
            if useri is not None:
                login(req ,useri)
                params={'name':Username , 'ap':allprods}
                return render(req,'home.html',params) 
        else :
            username=req.POST.get('iName')
            password=req.POST.get('iPass')
            checkpass=req.POST.get('iPass2')
            gender=req.POST.get('iGen')
            if(password!=checkpass):
                return HttpResponse("YOUR PASSWORDS DON'T MATCH ")
            else :
                user = User.objects.create_user(username, gender,password)
                ap={'ap':allprods}
                user.save()
                return render(req,'home.html',ap)
    


        
            
    
    ap={'ap':allprods}    
    return render(req,'home.html',ap)


def AddtoList(req):
    if req.method=='POST':
        p=Product()
        p.product_name=req.POST.get('pname')
        p.product_category=req.POST.get('pcate')
        p.product_price=req.POST.get('ppric')
        p.product_desc=req.POST.get('pdesc')    
        if len(req.FILES)!=0:
            p.product_image=req.FILES['imagica']
        p.save()
        return render(req,'insert.html')
    
    return render(req,'insert.html')    



def Lnout(req):
    logout(req)
    return redirect('home')

def F(req):
    return render(req,'about.html')    