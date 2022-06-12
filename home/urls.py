from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:id>', views.detail, name="detail"),
    path('esthaniye/', views.esthaniye, name='esthaniye'),
    path('rajnitic/', views.rajnitic, name='rajnitic'),
    path('samsamyak/', views.samsamyak, name='samsamyak'),
    path('khelkud/', views.khelkud, name='khelkud'),
    path('antarastriye/', views.antarastriye, name='antarastriye'),
    path('suchana/', views.suchana, name='suchana'),
    path('sowasthya/', views.sowasthya, name='sowasthya'),
    path('bichar/', views.bichar, name='bichar'),
    path('rochak/', views.rochak, name='rochak'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
