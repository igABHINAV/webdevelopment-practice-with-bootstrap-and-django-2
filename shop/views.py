import imp
from itertools import product
from django.shortcuts import render
from .models import Product
import math
# Create your views here.
def index(req):
    # p=Product.objects.all()
    # n=len(p)
    
    allprods=[]
    c=Product.objects.values('product_category')
    cat={item['product_category'] for item in c}
    print(c)
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