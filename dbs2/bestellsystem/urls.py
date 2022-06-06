from ast import Index
from operator import index
from django.urls import path
from bestellsystem.views import index,gehaltserhoehung,gehaltskürzung,mitarbeiter
app_name = "bestellsystem"

urlpatterns = [
    path('mitarbeiter/<int:mitarbeiter_id>',index, name='index'),
    path('mitarbeiter/',mitarbeiter, name='mitarbeiter'),
    
    path('mitarbeiter/<int:mitarbeiter_id>/gehaltserhoehung/<int:floatvalue>',gehaltserhoehung,name='gehaltserhoehung'), #callprocedure positiver fall
    path('mitarbeiter/<int:mitarbeiter_id>/gehaltskuerzung/<int:floatvalue>',gehaltskürzung,name='gehaltskürzung')      #callprocedure negativer fall
]
