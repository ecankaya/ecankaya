from django.contrib import admin
from .models import Mitarbeiter,Artikel,Geschaeftsstelle,Getraenk,Menue,Hauptspeise,Beilage,Artikelbestellung,Gehaltsklasse,Bestellung
# Register your models here.

admin.site.register(Mitarbeiter)
admin.site.register(Artikel)
admin.site.register(Geschaeftsstelle)
admin.site.register(Getraenk)
admin.site.register(Beilage)
admin.site.register(Hauptspeise)
admin.site.register(Gehaltsklasse)
admin.site.register(Bestellung)
