from sqlite3 import Cursor
from django import http
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.db import DatabaseError, connections

# Create your views here.
def index(request, mitarbeiter_id):
    with connections['DBS2'].cursor() as c:
        c.execute(f'SELECT * FROM MITARBEITER WHERE mitarbeiter_id = {mitarbeiter_id}')
        return HttpResponse (dictfetchall(c))
    
def mitarbeiter(request):
    with connections['DBS2'].cursor() as c:
        c.execute(f'SELECT * FROM MITARBEITER ')
        return render(request,'bestellsystem/mitarbeiters.html',{
            'mitarbeiterListe' : dictfetchall(c),
        })

def artikel(request):
    with connections['DBS2'].cursor() as c:
        c.execute(f'SELECT * FROM ARTIKEL ')
        return render(request,'bestellsystem/artikels.html',{
            'artikelliste' : dictfetchall(c),
        })

def bestellungen(request):
    with connections['DBS2'].cursor() as c:
        c.execute(f'SELECT * FROM Bestellung')
        return render(request,'bestellsystem/bestellungen.html',{
            'bestellliste' : dictfetchall(c),
        })

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def gehaltserhoehung(request,mitarbeiter_id,floatvalue):
    with connections['DBS2'].cursor() as c:
        try:
            c.callproc(f'gehaltserhoehung',[mitarbeiter_id,1+(floatvalue/100)])
        except DatabaseError as E:
            return HttpResponse(E)
        return HttpResponse('success')

def gehaltskürzung(request,mitarbeiter_id,floatvalue):
    with connections['DBS2'].cursor() as c:
        try:
            c.callproc(f'gehaltserhoehung',[mitarbeiter_id,1-(floatvalue/100)])
        except DatabaseError as E:
            return HttpResponse(E)
        return HttpResponse('success?')


