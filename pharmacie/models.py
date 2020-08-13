# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.db import models
import datetime
import time
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

def upload_logo(self, filename):
    # verification de l'extension
    real_name, extension = os.path.splitext(filename)
    name = str(int(time.time())) + extension
    return "logos/" + self.id + ".jpeg"


class Fournisseur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    num_licence = models.CharField(max_length=255)
    pays = CountryField(blank_label='(Préciser Le Pays)')
    adresse = models.CharField(max_length=255)
    contact1 = PhoneNumberField(help_text="+22545485648")  # CharField(max_length=50, verbose_name="TELEPHONE 1")
    contact2 = PhoneNumberField(help_text="+22545485648", blank=True)
    faxe = models.CharField(max_length=50, verbose_name="FAXE", blank=True)
    email = models.EmailField(max_length=120, blank=True, verbose_name="ADRESSE EMAIL")
    siteweb = models.CharField(max_length=120, blank=True, verbose_name="SITE WEB")
    logo = models.ImageField(verbose_name="Logo", upload_to=upload_logo, blank=True)
    description = models.TextField()
    add_le = models.DateTimeField(auto_now_add=True)
    update_le = models.DateTimeField(auto_now=True)
    objects = models.Manager()


    def __str__(self):
        return self.nom + " " +self.adresse

class CompteFournisseur(models.Model):
    Type = (
        ("1", "Credit"),
        ("2", "Debit")
    )
    id = models.AutoField(primary_key=True)
    fournisseur_id = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    type_transaction = models.CharField(choices=Type, max_length=15)
    montant_transaction = models.DecimalField(max_digits=10, decimal_places=2)
    date_transaction = models.DateField()
    mode_payement = models.CharField(max_length=255)
    add_le = models.DateTimeField(auto_now_add=True)
    update_le = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class BanqueFrs(models.Model):
    id = models.AutoField(primary_key=True)
    fournisseur_id = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    num_compte_bancaire = models.CharField(max_length=255)
    ifsc_num = models.CharField(max_length=255)
    add_le = models.DateTimeField(auto_now_add=True)
    update_le = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Produit(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    categorie = models.CharField(max_length=255)
    prix_achat = models.DecimalField(max_digits=10, decimal_places=2)
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2)
    c_gst = models.CharField(max_length=255)
    s_gst = models.CharField(max_length=255)
    num_lot = models.IntegerField(default=0)
    num_produit = models.IntegerField(default=0)
    date_production = models.DateField()
    date_expiration = models.DateField()
    fournisseur_id = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    description = models.TextField()
    total_stock = models.IntegerField(default=0)
    qte_stock = models.IntegerField(default=0)
    add_le = models.DateTimeField(auto_now_add=True)
    update_le = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class DetailProd(models.Model):
    id  = models.AutoField(primary_key=True)
    produit_id = models.ForeignKey(Produit, on_delete=models.CASCADE)
    salt_name = models.CharField(max_length=255)
    salt_qte_type = models.IntegerField(default=0)
    description = models.TextField()
    add_le = models.DateTimeField(auto_now_add=True)
    update_le = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Employer(models.Model):
    id  = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    contact1 = PhoneNumberField(help_text="+22545485648")  # CharField(max_length=50, verbose_name="TELEPHONE 1")
    contact2 = PhoneNumberField(help_text="+22545485648", blank=True)
    adresse = models.CharField(max_length=255)
    embauche_le = models.DateField()
    add_le = models.DateTimeField(auto_now_add=True)
    update_le = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class SalaireEmp(models.Model):
    id = models.AutoField(primary_key=True)
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    salare = models.DecimalField(max_digits=10, decimal_places=2)
    salaire_date = models.DateField()
    add_le = models.DateTimeField(auto_now_add=True)
    update_le = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class BanqueEmp(models.Model):
    id = models.AutoField(primary_key=True)
    emplyer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    num_compte_bancaire = models.CharField(max_length=255)
    ifsc_num = models.CharField(max_length=255)
    add_le = models.DateTimeField(auto_now_add=True)
    update_le = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    contact1 = PhoneNumberField(help_text="+22545485648")  # CharField(max_length=50, verbose_name="TELEPHONE 1")
    contact2 = PhoneNumberField(help_text="+22545485648", blank=True)
    adresse = models.CharField(max_length=255)
    add_le = models.DateTimeField(auto_now_add=True)
    update_le = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class RequeteClt(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    add_le = models.DateTimeField(auto_now_add=True)
    update_le = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Facture(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    add_le = models.DateTimeField(auto_now_add=True)
    update_le = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class DetailFacture(models.Model):
    id = models.AutoField(primary_key=True)
    facture_id = models.ForeignKey(Facture, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    qte = models.IntegerField(default=0)
    add_le = models.DateTimeField(auto_now_add=True)
    update_le = models.DateTimeField(auto_now=True)
    objects = models.Manager()


# Create your models here.
