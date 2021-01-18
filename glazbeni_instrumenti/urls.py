
from django.urls import path, re_path, include
from . import views
from .views import *
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from django_openapi import OpenAPI
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.static import static
from . import settings
from django.views.defaults import server_error

from django.views.generic import TemplateView
from django.views.defaults import page_not_found, server_error




schema_view = get_schema_view(
   openapi.Info(
      title="Glazbeni instrumenti",
      default_version='v3',
      description="Opis nekih glazbenih instrumenata.",
      public=True,
   ),
   
   permission_classes=(permissions.AllowAny,)
)


urlpatterns = [
    path('database/', ImportData.as_view(), name='database'),
    path('index/', ForIndex.as_view(), name='index '),
    path('instrumenti/',FrontPage.as_view(),name="singleGroup"),
    path('instrument/<id>/',SpecificInstrument.as_view(),name="instrument"),
    path('specification/<id>/',Specification.as_view(),name="specification"),
    path('kolekcija/<id>/',Kolekcija.as_view(),name="Kolekcija"),
    path('kolekcija/<id>/picture/',KolekcijaSlika.as_view(),name="KolekcijaSlika"),
    path('child/<id>/',Child.as_view(),name="child"),
    path('type/<species>/',Type.as_view(),name="type"),
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)