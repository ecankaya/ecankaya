# Generated by Django 4.0.4 on 2022-06-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('artikel_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('kallorien', models.BigIntegerField(blank=True, null=True)),
                ('preis', models.FloatField()),
                ('allergencode', models.CharField(blank=True, max_length=8, null=True)),
                ('typ', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'artikel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Artikelbestellung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anzahl', models.BigIntegerField(blank=True, null=True)),
                ('schaerfeklasse', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'artikelbestellung',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Beilage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scovil', models.BigIntegerField(blank=True, null=True)),
                ('groeße', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'beilage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bestellung',
            fields=[
                ('bestellung_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nettogesamtpreis', models.FloatField(blank=True, null=True)),
                ('bruttogesamtpreis', models.FloatField(blank=True, null=True)),
                ('waehrung', models.CharField(blank=True, max_length=3, null=True)),
                ('bezahlmethode', models.CharField(blank=True, max_length=3, null=True)),
                ('mitnehmen', models.CharField(blank=True, max_length=1, null=True)),
                ('bestellzeit', models.DateTimeField(blank=True, null=True)),
                ('allergencode', models.CharField(blank=True, max_length=8, null=True)),
                ('status', models.BigIntegerField(blank=True, null=True)),
                ('payback', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bestellung',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField(blank=True, null=True)),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gehaltsklasse',
            fields=[
                ('geh_klasse', models.BigAutoField(primary_key=True, serialize=False)),
                ('min_gehalt', models.FloatField(blank=True, null=True)),
                ('max_gehalt', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'gehaltsklasse',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Geschaeftsstelle',
            fields=[
                ('geschaeftsstelle_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('ort', models.CharField(max_length=50)),
                ('land', models.CharField(max_length=50)),
                ('arbeitszeitvolumen', models.BigIntegerField()),
                ('anzahlbestellungen', models.BigIntegerField(blank=True, null=True)),
                ('nebenkosten', models.FloatField(blank=True, null=True)),
                ('umsatz', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'geschaeftsstelle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Getraenk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eis', models.CharField(blank=True, max_length=4, null=True)),
                ('groeße', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'getraenk',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hauptspeise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scovil', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hauptspeise',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Menue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scovil', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'menue',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mitarbeiter',
            fields=[
                ('mitarbeiter_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('vorname', models.CharField(max_length=50)),
                ('ort', models.CharField(max_length=50)),
                ('straße', models.CharField(blank=True, max_length=50, null=True)),
                ('telefon', models.BigIntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('gehalt', models.FloatField()),
                ('arbeitszeit', models.BigIntegerField()),
            ],
            options={
                'db_table': 'mitarbeiter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Schaerfescala',
            fields=[
                ('schaerfeklasse', models.BigIntegerField(primary_key=True, serialize=False)),
                ('scovil_min', models.BigIntegerField(blank=True, null=True)),
                ('scovil_max', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'schaerfescala',
                'managed': False,
            },
        ),
    ]
