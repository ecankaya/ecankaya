# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Artikel(models.Model):
    artikel_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    kallorien = models.BigIntegerField(blank=True, null=True)
    preis = models.FloatField()
    allergencode = models.CharField(max_length=8, blank=True, null=True)
    typ = models.CharField(max_length=1)

    class Meta:
        managed = True
        db_table = 'artikel'


class Artikelbestellung(models.Model):
    artikel = models.ForeignKey(Artikel, models.DO_NOTHING, blank=True, null=True)
    bestellung = models.ForeignKey('Bestellung', models.DO_NOTHING, blank=True, null=True)
    anzahl = models.BigIntegerField(blank=True, null=True)
    schaerfeklasse = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'artikelbestellung'


class Beilage(models.Model):
    artikel = models.ForeignKey(Artikel, models.DO_NOTHING, blank=True, primary_key=True)
    schaerfeklasse = models.ForeignKey('Schaerfescala', models.DO_NOTHING, db_column='schaerfeklasse', blank=True, null=True)
    scovil = models.BigIntegerField(blank=True, null=True)
    groeße = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'beilage'


class Bestellung(models.Model):
    bestellung_id = models.BigAutoField(primary_key=True)
    nettogesamtpreis = models.FloatField(blank=True, null=True)
    bruttogesamtpreis = models.FloatField(blank=True, null=True)
    waehrung = models.CharField(max_length=3, blank=True, null=True)
    bezahlmethode = models.CharField(max_length=3, blank=True, null=True)
    mitnehmen = models.CharField(max_length=1, blank=True, null=True)
    bestellzeit = models.DateTimeField(blank=True, null=True)
    allergencode = models.CharField(max_length=8, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    payback = models.BigIntegerField(blank=True, null=True)
    mitarbeiter = models.ForeignKey('Mitarbeiter', models.DO_NOTHING, blank=True, null=True)
    geschaeftsstelle = models.ForeignKey('Geschaeftsstelle', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bestellung'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'


class Gehaltsklasse(models.Model):
    geh_klasse = models.BigAutoField(primary_key=True)
    min_gehalt = models.FloatField(blank=True, null=True)
    max_gehalt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'gehaltsklasse'


class Geschaeftsstelle(models.Model):
    geschaeftsstelle_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    ort = models.CharField(max_length=50)
    land = models.CharField(max_length=50)
    arbeitszeitvolumen = models.BigIntegerField()
    anzahlbestellungen = models.BigIntegerField(blank=True, null=True)
    nebenkosten = models.FloatField(blank=True, null=True)
    umsatz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'geschaeftsstelle'


class Getraenk(models.Model):
    artikel = models.ForeignKey(Artikel, models.DO_NOTHING, blank=True, primary_key=True)
    eis = models.CharField(max_length=4, blank=True, null=True)
    groeße = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'getraenk'


class Hauptspeise(models.Model):
    artikel = models.ForeignKey(Artikel, models.DO_NOTHING, blank=True, primary_key=True)
    schaerfeklasse = models.ForeignKey('Schaerfescala', models.DO_NOTHING, db_column='schaerfeklasse', blank=True, null=True)
    scovil = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hauptspeise'


class Menue(models.Model):
    artikel = models.ForeignKey(Artikel, models.DO_NOTHING, blank=True, primary_key=True)
    hauptspeise = models.ForeignKey(Artikel, models.DO_NOTHING,related_name='m_hauptspeise', db_column='hauptspeise')
    beilage = models.ForeignKey(Artikel, models.DO_NOTHING,related_name='m_beilage', db_column='beilage', blank=True, null=True)
    getraenk = models.ForeignKey(Artikel, models.DO_NOTHING,related_name='m_getraenk', db_column='getraenk', blank=True, null=True)
    scovil = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'menue'


class Mitarbeiter(models.Model):
    mitarbeiter_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    vorname = models.CharField(max_length=50)
    ort = models.CharField(max_length=50)
    straße = models.CharField(max_length=50, blank=True, null=True)
    telefon = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    gehalt = models.FloatField()
    geh_klasse = models.ForeignKey(Gehaltsklasse, models.DO_NOTHING, db_column='geh_klasse', blank=True, null=True)
    arbeitszeit = models.BigIntegerField()
    geschaeftsstelle = models.ForeignKey(Geschaeftsstelle, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mitarbeiter'


class Schaerfescala(models.Model):
    schaerfeklasse = models.BigIntegerField(primary_key=True)
    scovil_min = models.BigIntegerField(blank=True, null=True)
    scovil_max = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'schaerfescala'
