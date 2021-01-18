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
from .serializers import SerializerInstrumenata
import urllib
from datetime import timedelta
from rest_framework.decorators import api_view
from django.core.cache import cache
import time 
from rest_framework import serializers
from django.core.files.base import ContentFile
from rest_framework import status
from django.shortcuts import redirect

from django.utils.html import urlize

from django.http import HttpResponse
from urllib.request import urlopen 

import requests
from django.views.decorators.cache import cache_page
import base64

from PIL import Image
from io import BytesIO
from datetime import datetime 


def my_test_500_view(request):
    # Return an "Internal Server Error" 500 response code.
    return HttpResponse(status=500)

def my_test_404_view(request):
    # Return an "Internal Server Error" 500 response code.
    return HttpResponse(status=404)




class SerializerData(serializers.Serializer):
    naziv = serializers.CharField()
    wikipedija = serializers.CharField()
    vrsta_instrumenta = serializers.CharField()
    zemlja_podrijetla = serializers.CharField()
    stoljeće_pojave = serializers.IntegerField()
    glazbeni_žanrovi = serializers.ListField(child=serializers.CharField())
    način_sviranja = serializers.CharField()
    najpoznatiji_izvođači = serializers.ListField(child=serializers.CharField())
    najpoznatiji_proizvođači = serializers.ListField(child=serializers.CharField())
    dio  = serializers.CharField()
    materijal = serializers.CharField()

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

class FrontPage(APIView):

    def get(self, request):
        try:
            instrumenti = Instrumenti.objects.all()
            allData=[{  
                        '@context': {
                            "head":'https://schema.org/',
                            "image":"localhost:8000/kolekcija/" + str(instrument.dio1) + "/picture/",
                        },
                        '@type': 'Thing',
                        'naziv': instrument.naziv,
                        'link':{
                            "href": "/instrument/"+str(instrument.dio1)+"/",
                            "rel": "instrument",
                            "type": 'GET' 
                        }} for instrument in instrumenti]
            contex = {'data':allData}
            return Response({"status":"OK","message":"Fetched department object","response":allData},status=status.HTTP_200_OK)
        except:
            return Response({"status": "Not Found",  "message": "Department with the provided ID doesn't exist",  "reponse": {}},status=status.HTTP_404_NOT_FOUND)

class SpecificInstrument(APIView):

    def get(self, request,id):
        try:
            instrumenti = Instrumenti.objects.all().filter(dio1=id)
            if(not Instrumenti.objects.all().filter(dio1=id)):
                return Response({"status": "Not Found",  "message": "Department with the provided ID doesn't exist",  "reponse": {}},status=status.HTTP_404_NOT_FOUND)

            allData={  
                        'id': instrumenti[0].dio1,
                        '@context': {
                            "head":'https://schema.org/',
                            "image":"localhost:8000/kolekcija/" + str(instrumenti[0].dio1) + "/picture/",
                        },
                        '@type': 'Thing',
                        'naziv': instrumenti[0].naziv,
                        'links':[{
                            "href": "/specification/"+str(instrumenti[0].dio1)+"/",
                            "rel": "specification",
                            "type": 'GET'
                        },{
                            "href": "/child/"+str(instrumenti[0].dio1)+"/",
                            "rel": "specification",
                            "type": 'GET'
                        }]
                        }
            contex = {'data':allData}
            return Response({"status":"OK","message":"Fetched department object","response":allData},status=status.HTTP_200_OK)
        except:
            return Response({"status": "Not Found",  "message": "Department with the provided ID doesn't exist",  "reponse": {}},status=status.HTTP_400_BAD_REQUEST)

class Specification(APIView):

    def get(self, request,id):
        try:
            instrumenti = Instrumenti.objects.all().filter(dio1=id)
            allData={  
                        'id': instrumenti[0].dio1,
                        '@context': {
                            "head":'https://schema.org/',
                            "image":"localhost:8000/kolekcija/" + str(instrumenti[0].dio1) + "/picture/",
                        },
                        '@type': 'Thing',
                        'naziv': instrumenti[0].naziv,
                        'links':[{
                            "href": "https://hr.wikipedia.org/wiki/"+str(instrumenti[0].wikipedija),
                            "rel": "wikipedija",
                            "type": 'GET'
                        },
                        {"href": "/type/"+ instrumenti[0].vrsta_instrumenta+"/",
                        "rel": "Vrsta instrumenta",
                        "type": 'GET'}],
                        'zemlja_podrijetla': instrumenti[0].zemlja_podrijetla,
                        'stoljeće_pojave': instrumenti[0].stoljeće_pojave,
                        'glazbeni_žanrovi': {
                            '@context': {
                                "head":'https://schema.org/',
                                'name':instrumenti[0].glazbeni_žanrovi,
                            },
                            '@type': 'MusicRecording'},
                        'način_sviranja': instrumenti[0].način_sviranja,
                        'najpoznatiji_izvođači': instrumenti[0].najpoznatiji_izvođači,
                        'najpoznatiji_proizvođači': instrumenti[0].najpoznatiji_proizvođači
                        }
            contex = {'data':allData}
            return Response({"status":"OK","message":"Fetched department object","response":allData},status=status.HTTP_200_OK)
        except:
            return Response({"status": "Not Found",  "message": "Department with the provided ID doesn't exist",  "reponse": {}},status=status.HTTP_400_BAD_REQUEST)




class Type(APIView):

    def get(self, request,species):
        try:
            instrumenti = Instrumenti.objects.all().filter(vrsta_instrumenta=species)
            if(not Instrumenti.objects.all().filter(vrsta_instrumenta=species)):
                return Response({"status": "Not Found",  "message": "Department with the provided ID doesn't exist",  "reponse": {}},status=status.HTTP_404_NOT_FOUND)

            allData=[{  
                        '@context': {
                            "head":'https://schema.org/',
                            "image":"localhost:8000/kolekcija/" + str(instrumenti[0].dio1) + "/picture/",
                        },
                        '@type': 'Thing',
                        'naziv': instrument.naziv,
                        'link':{
                            "href": "/instrument/"+str(instrument.dio1)+"/",
                            "rel": "instrument",
                            "type": 'GET' 
                        }} for instrument in instrumenti]
            contex = {'data':allData}
            return Response({"status":"OK","message":"Fetched department object","response":allData},status=status.HTTP_200_OK)
        except:
            return Response({"status": "Not Found",  "message": "Department with the provided ID doesn't exist",  "reponse": {}},status=status.HTTP_400_BAD_REQUEST)

class Child(APIView):

    def get(self, request,id):
        try:
            dijelovi = Dijelovi.objects.all().filter(id1=id)
            if(not Dijelovi.objects.all().filter(id1=id)):
                return Response({"status": "Not Found",  "message": "Department with the provided ID doesn't exist",  "reponse": {}},status=status.HTTP_404_NOT_FOUND)

            instrument = Instrumenti.objects.all()
            allData=[
                    
                        {   
                        'naziv': instrument.filter(dio1=id)[0].naziv,
                        'links':[{
                            "href": "/specification/"+str(id)+"/",
                            "rel": "specification",
                            "type": 'GET'
                        },
                        {
                            "href": "/child/"+str(id)+"/",
                            "rel": "child-put",
                            "type": 'PUT'
                        },
                        {
                            "href": "/child/"+str(id)+"/",
                            "rel": "child-delete",
                            "type": 'DELETE'
                        },
                        {
                            "href": "/child/"+str(id)+"/",
                            "rel": "child-delete",
                            "type": 'POST'
                        },],
                        'dio':i.dio,
                        'materijal':i.materijal} for i in dijelovi]
            contex = {'data':allData}
            return Response({"status":"OK","message":"Fetched department object","response":allData},status=status.HTTP_200_OK)
        except:
            return Response({"status": "Not Found",  "message": "Department with the provided ID doesn't exist",  "reponse": {}},status=status.HTTP_400_BAD_REQUEST)


    def post(self, request,id):    
        try:
            dijelovi = Dijelovi.objects.all().filter(id1=id)
            if(not Dijelovi.objects.all().filter(id1=id)):
                return Response({"status": "Not Found",  "message": "Department with the provided ID doesn't exist",  "reponse": {}},status=status.HTTP_404_NOT_FOUND)

            instrument = Instrumenti.objects.all()
            dio=json.loads(request.body)["dio"]
            materijal=json.loads(request.body)["materijal"]
            if(Dijelovi.objects.all().filter(id1=id, dio=dio, materijal=materijal)):
                return Response({"status": "Bad request",  "message": "Already exist",  "reponse": {}},status=status.HTTP_400_BAD_REQUEST)

            Dijelovi.objects.create(id1=id, dio=dio, materijal=materijal)
            dijelovi = Dijelovi.objects.all().filter(id1=id)

            allData=[       
                    {   
                        
                        'dio':i.dio,
                        'materijal':i.materijal} for i in dijelovi]

            
            return Response({"status":"CREATED","message":"Fetched department object","response":allData},status=status.HTTP_201_CREATED)
        except:
            return Response({"status": "Not Found",  "message": "Department with the provided ID doesn't exist",  "reponse": {}})

    def put(self, request,id):    
        try:
            dijelovi = Dijelovi.objects.all().filter(id1=id)
            if(not Dijelovi.objects.all().filter(id1=id)):
                return Response({"status": "Not Found",  "message": "Department with the provided ID doesn't exist",  "reponse": {}},status=status.HTTP_404_NOT_FOUND)
            instrument = Instrumenti.objects.all()
            dio=json.loads(request.body)["dio"]
            materijal=json.loads(request.body)["materijal"]
            if(not Dijelovi.objects.all().filter(id1=id, dio=dio)):
                return Response({"status": "Bad request",  "message": "Department don't exist",  "reponse": {}},status=status.HTTP_400_BAD_REQUEST)
            Dijelovi.objects.all().filter(id1=id, dio=dio).delete()
            Dijelovi.objects.create(id1=id, dio=dio, materijal=materijal)
            allData=[       
                    {                           
                        'dio':i.dio,
                        'materijal':i.materijal} for i in dijelovi]
            
            return Response({"status":"OK","message":"Fetched department object","response":allData},status=status.HTTP_200_OK)
        except:
            return Response({"status": "Not Found",  "message": "Department with the provided ID doesn't exist",  "reponse": {}},status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request,id):    
        try:
            dijelovi = Dijelovi.objects.all().filter(id1=id)
            if(not Dijelovi.objects.all().filter(id1=id)):
                return Response({"status": "Not Found",  "message": "Department with the provided ID doesn't exist",  "reponse": {}},status=status.HTTP_404_NOT_FOUND)
            
            instrument = Instrumenti.objects.all()
            dio=json.loads(request.body)["dio"]
            materijal=json.loads(request.body)["materijal"]
            if(not Dijelovi.objects.all().filter(id1=id, dio=dio, materijal=materijal)):
                return Response({"status": "Bad request",  "message": "Department don't exist",  "reponse": {}},status=status.HTTP_400_BAD_REQUEST)
            Dijelovi.objects.all().filter(id1=id, dio=dio, materijal=materijal).delete()
            dijelovi = Dijelovi.objects.all().filter(id1=id)
            allData=[       
                    {   
                        'dio':i.dio,
                        'materijal':i.materijal} for i in dijelovi]
            
            return Response({"status":"No content","message":"Fetched department object","response":allData},status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"status": "Not Found",  "message": "Department with the provided ID doesn't exist",  "reponse": {}},status=status.HTTP_404_NOT_FOUND)

class KolekcijaSlika(APIView):
    def get(self, request,id):
        try:
            instrumenti = Instrumenti.objects.all().filter(dio1=id)
            try:
                nova = Privremena.objects.get(id1=id)
                vrijeme = Vrijeme.objects.update(id1=id, time = datetime.now())
                sada = Vrijeme.objects.get(id1=id)
                if(nova.timestamp_end>sada.time):
                    print(1)
                    with open(nova.img, "rb") as f:
                        response1 = HttpResponse(f.read(), content_type="image/jpeg")
                        response1['Content-Disposition'] = 'image; filename="image.jpeg"'
                        return response1
                else:
                    time = datetime.now() + timedelta(minutes=5)
                    print(2)
                    q = Privremena.objects.filter(id1=id).update(timestamp_end=time)
                    with open(nova.img, "rb") as f:
                        response1 = HttpResponse(f.read(), content_type="image/jpeg")
                        response1['Content-Disposition'] = 'image; filename="image.jpeg"'
                        return response1
            except:
                response = requests.get('https://hr.wikipedia.org/api/rest_v1/page/summary/'+instrumenti[0].naziv)
                data = response.json()

                image = base64.b64encode(requests.get(data['originalimage']['source']).content)
                k = base64.b64decode(image)

                slika = 'glazbeni_instrumenti\slike\ '+ id + '.jpeg'
                t = datetime.now() + timedelta(minutes=5)
                
                Privremena.objects.create(id1=id, img=slika, timestamp_end=t)
                filehandle = open(slika, 'wb')
                filehandle.write(k)
                filehandle.close()
                
                
                with open(slika, "rb") as f:
                    response1 = HttpResponse(f.read(), content_type="image/jpeg")
                    response1['Content-Disposition'] = 'image; filename="image.jpeg"'
                    return response1
        except:
            return Response({"status": "Not Found",  "message": "Department with the provided ID doesn't exist",  "reponse": {}},status=status.HTTP_400_BAD_REQUEST)

class Kolekcija(APIView):

    def get(self, request,id):
        try:
            instrumenti = Instrumenti.objects.all().filter(dio1=id)
            allData={  
                        'id': instrumenti[0].dio1,
                        '@context': {
                            "head":'https://schema.org/',
                            "image":"localhost:8000/kolekcija/" + str(instrument.dio1) + "/picture/",
                        },
                        '@type': 'Thing',
                        'naziv': instrumenti[0].naziv,
                        'links':[{
                            "href": "https://hr.wikipedia.org/wiki/"+str(instrumenti[0].wikipedija),
                            "rel": "wikipedija",
                            "type": 'GET'
                        },
                        {"href": "/type/"+ instrumenti[0].vrsta_instrumenta+"/",
                        "rel": "Vrsta instrumenta",
                        "type": 'GET'}],
                        'slika': "/kolekcija/"+ str(instrumenti[0].dio1)+"/picture/"
                        }
            contex = {'data':allData}
            return Response({"status":"OK","message":"Fetched department object","response":allData},status=status.HTTP_200_OK)
        except:
            return Response({"status": "Not Found",  "message": "Department with the provided ID doesn't exist",  "reponse": {}},status=status.HTTP_400_BAD_REQUEST)


#status.HTTP_200_OK
#status.HTTP_201_CREATED
#status.HTTP_204_NO_CONTENT
#status.HTTP_400_BAD_REQUEST
#status.HTTP_404_NOT_FOUND
#status.HTTP_500_INTERNAL_SERVER_ERROR
#status.HTTP_501_NOT_IMPLEMENTED