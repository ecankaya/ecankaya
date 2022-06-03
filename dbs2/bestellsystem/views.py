
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connections

# Create your views here.
def index(request, mitarbeiter_id):
    with connections['DBS2'].cursor() as c:
        c.execute(f'SELECT * FROM MITARBEITER WHERE mitarbeiter_id = {mitarbeiter_id}')
        return HttpResponse (dictfetchall(c))
    

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def gehaltserhoehung(request,mitarbeiter_id,floatvalue):
    with connections['DBS2'].cursor() as c:
        c.callproc(f'gehaltserhoehung',[mitarbeiter_id,1+(floatvalue/100)])
        return HttpResponse('success')

def gehaltskürzung(request,mitarbeiter_id,floatvalue):
    with connections['DBS2'].cursor() as c:
        c.callproc(f'gehaltserhoehung',[mitarbeiter_id,1-(floatvalue/100)])
        return HttpResponse()


