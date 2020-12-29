from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import json
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from smtplib import SMTPRecipientsRefused
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from itertools import chain
import numbers
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

class ImportData(APIView):

    def get(self, request):
        dijelovi = Dijelovi.objects.all()
        instrument = Instrumenti.objects.all()
        allData = Sve.objects.none()
        allData=[{  
                    'naziv': instrument.filter(dio1=i.id1)[0].naziv,
                    'wikipedija': instrument.filter(dio1=i.id1)[0].wikipedija,
                    'vrsta_instrumenta': instrument.filter(dio1=i.id1)[0].vrsta_instrumenta,
                    'zemlja_podrijetla': instrument.filter(dio1=i.id1)[0].zemlja_podrijetla,
                    'stoljeće_pojave': instrument.filter(dio1=i.id1)[0].stoljeće_pojave,
                    'glazbeni_žanrovi': instrument.filter(dio1=i.id1)[0].glazbeni_žanrovi,
                    'način_sviranja': instrument.filter(dio1=i.id1)[0].način_sviranja,
                    'najpoznatiji_izvođači': instrument.filter(dio1=i.id1)[0].najpoznatiji_izvođači,
                    'najpoznatiji_proizvođači': instrument.filter(dio1=i.id1)[0].najpoznatiji_proizvođači,
                    'dio':i.dio,
                    'materijal':i.materijal} for i in dijelovi]

        if(request.is_ajax()):
            allData = [Sve]
            inst = instrument
            dijelov = dijelovi
            ulaz = request.GET['fname']
            vrsta = request.GET['vrsta']
            allData1=[{  
                    'naziv': instrument.filter(dio1=i.id1)[0].naziv,
                    'wikipedija': instrument.filter(dio1=i.id1)[0].wikipedija,
                    'vrsta_instrumenta': instrument.filter(dio1=i.id1)[0].vrsta_instrumenta,
                    'zemlja_podrijetla': instrument.filter(dio1=i.id1)[0].zemlja_podrijetla,
                    'stoljeće_pojave': instrument.filter(dio1=i.id1)[0].stoljeće_pojave,
                    'glazbeni_žanrovi': instrument.filter(dio1=i.id1)[0].glazbeni_žanrovi,
                    'način_sviranja': instrument.filter(dio1=i.id1)[0].način_sviranja,
                    'najpoznatiji_izvođači': instrument.filter(dio1=i.id1)[0].najpoznatiji_izvođači,
                    'najpoznatiji_proizvođači': instrument.filter(dio1=i.id1)[0].najpoznatiji_proizvođači,
                    'dio':i.dio,
                    'materijal':i.materijal} for i in dijelovi]
            for data1 in allData1:
                if((vrsta=='naziv' or vrsta == 'svi')and data1.get('naziv')==ulaz):
                    allData.append(data1)
                if((vrsta=='Wiki' or vrsta == 'svi')and data1.get('wikipedija')==ulaz):
                    allData.append(data1)
                if((vrsta=='vrsta_inst'or vrsta == 'svi') and data1.get('vrsta_instrumenta')==ulaz):
                    allData.append(data1)
                if((vrsta=='zemlja' or vrsta == 'svi')and data1.get('zemlja_podrijetla')==ulaz):
                    allData.append(data1)
                if((vrsta=='st' or vrsta == 'svi') and ulaz.isdigit()):
                    if(data1.get('stoljeće_pojave') ==int(ulaz)):
                        allData.append(data1)
                if((vrsta=='nacin' or vrsta == 'svi')and data1.get('način_sviranja')==ulaz):
                    allData.append(data1)
                if((vrsta=='Dio' or vrsta == 'svi')and data1.get('dio')==ulaz):
                    allData.append(data1)
                if((vrsta=='mat' or vrsta == 'svi')and data1.get('materijal')==ulaz):
                    allData.append(data1)
                if((vrsta=='znr' or vrsta == 'svi')and ulaz in data1.get('glazbeni_žanrovi')):
                    allData.append(data1)
                if((vrsta=='izv' or vrsta == 'svi')and ulaz in data1.get('najpoznatiji_izvođači')):
                    allData.append(data1)
                if((vrsta=='pro' or vrsta == 'svi')and ulaz in data1.get('najpoznatiji_proizvođači')):
                    allData.append(data1)
            allData.pop(0)
                
        contex={'data':allData}
        #return Response(tablica.values())
        return render(request, "datatable.html",contex)
        #return JsonResponse(contex)

class ForIndex(APIView):

    def get(self, request):
        dijelovi = Dijelovi.objects.all()
        instrument = Instrumenti.objects.all()
        allData=[{  
                    'naziv': instrument.filter(dio1=i.id1)[0].naziv,
                    'wikipedija': instrument.filter(dio1=i.id1)[0].wikipedija,
                    'vrsta_instrumenta': instrument.filter(dio1=i.id1)[0].vrsta_instrumenta,
                    'zemlja_podrijetla': instrument.filter(dio1=i.id1)[0].zemlja_podrijetla,
                    'stoljeće_pojave': instrument.filter(dio1=i.id1)[0].stoljeće_pojave,
                    'glazbeni_žanrovi': instrument.filter(dio1=i.id1)[0].glazbeni_žanrovi,
                    'način_sviranja': instrument.filter(dio1=i.id1)[0].način_sviranja,
                    'najpoznatiji_izvođači': instrument.filter(dio1=i.id1)[0].najpoznatiji_izvođači,
                    'najpoznatiji_proizvođači': instrument.filter(dio1=i.id1)[0].najpoznatiji_proizvođači,
                    'dio':i.dio,
                    'materijal':i.materijal} for i in dijelovi]
        contex = {'data':allData}
        return render(request, "index.html", contex)
   