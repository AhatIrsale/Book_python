from django.contrib import admin
from django.contrib import admin
from .models import *

for m in [Utilisateur,Admin,contact,Categorie,Livre]:
    admin.site.register(m)
