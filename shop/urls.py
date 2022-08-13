from django.contrib import admin
from django.urls import path
#01332278971
from shop import views
urlpatterns = [
    path('',views.index,name='home' ),
    path('addtolist/',views.AddtoList,name='AddtoList'),
    path('logout/',views.Lnout,name='log_out'),
    path('features/',views.F,name='F')
]