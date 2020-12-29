from django.db import models
from django.contrib.postgres.fields import ArrayField
from django import forms



class Instrumenti(models.Model):
    naziv = models.CharField(max_length=255, primary_key=True, db_column='naziv')
    wikipedija = models.CharField(max_length=255, db_column='wikipedija')
    vrsta_instrumenta = models.CharField(max_length=255, db_column='vrsta_instrumenta')
    zemlja_podrijetla = models.CharField(max_length=255, db_column='zemlja_podrijetla')
    stoljeće_pojave = models.IntegerField(db_column='stoljeće_pojave')
    glazbeni_žanrovi = ArrayField(models.CharField(max_length=255), db_column='glazbeni_žanrovi')
    dio1 = models.IntegerField(db_column='dijelovi')
    način_sviranja = models.CharField(max_length=255, db_column='način_sviranja')
    najpoznatiji_izvođači = ArrayField(models.CharField(max_length=255, blank = True), db_column='najpoznatiji_izvođači')
    najpoznatiji_proizvođači = ArrayField(models.CharField(max_length=255, blank = True), db_column='najpoznatiji_proizvođači')
    
    class Meta:
       db_table = 'glazbeni_instrumenti'

class Dijelovi(models.Model):
    id1 = models.IntegerField(primary_key=True, db_column = 'id')
    dio  = models.CharField(max_length=255, db_column='dio')
    materijal = models.CharField(max_length=255, db_column='materijal')
    class Meta:
        db_table = 'dijelovi'

class Sve(models.Model):
    naziv = models.CharField(max_length=255, primary_key=True, db_column='naziv')
    wikipedija = models.CharField(max_length=255, db_column='wikipedija')
    vrsta_instrumenta = models.CharField(max_length=255, db_column='vrsta_instrumenta')
    zemlja_podrijetla = models.CharField(max_length=255, db_column='zemlja_podrijetla')
    stoljeće_pojave = models.IntegerField(db_column='stoljeće_pojave')
    glazbeni_žanrovi = ArrayField(models.CharField(max_length=255), db_column='glazbeni_žanrovi')
    način_sviranja = models.CharField(max_length=255, db_column='način_sviranja')
    najpoznatiji_izvođači = ArrayField(models.CharField(max_length=255, blank = True), db_column='najpoznatiji_izvođači')
    najpoznatiji_proizvođači = ArrayField(models.CharField(max_length=255, blank = True), db_column='najpoznatiji_proizvođači')
    dio  = models.CharField(max_length=255, db_column='dio')
    materijal = models.CharField(max_length=255, db_column='materijal')