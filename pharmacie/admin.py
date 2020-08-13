from django.contrib import admin
from .models import Employer, BanqueEmp, CompteFournisseur, DetailFacture, BanqueFrs, DetailProd, RequeteClt, SalaireEmp, Produit, Facture, Client, Fournisseur



admin.site.register(Employer)
admin.site.register(BanqueEmp)
admin.site.register(BanqueFrs)
admin.site.register(CompteFournisseur)
admin.site.register(DetailFacture)
admin.site.register(DetailProd)
admin.site.register(RequeteClt)
admin.site.register(SalaireEmp)
admin.site.register(Produit)
admin.site.register(Fournisseur)
admin.site.register(Client)
admin.site.register(Facture)
# Register your models here.
