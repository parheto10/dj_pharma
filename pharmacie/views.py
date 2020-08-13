from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from pharmacie.models import Fournisseur, BanqueFrs, Produit
from .serializers import FournisseurSerializer, BanqueFrsSerializer, ProduitSerializer


class FournisseurViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        fournisseur = Fournisseur.objects.all()
        serializer = FournisseurSerializer(fournisseur, many=True, context = { 'request' : request})
        response_dict = {"error":False, "message":"Liste des Fournisseurs", "data":serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = FournisseurSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Données Fournisseur Ajouter Avec Succès"}
        except:
            dict_response = {"error": True, "message": "Une Erreur est survenue lors de l'enregistrement des données Fournisseur"}
        return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = Fournisseur.objects.all()
            fournisseur = get_object_or_404(queryset, pk=pk)
            serializer = FournisseurSerializer(fournisseur, data=request.data, context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Données Fournisseur Modifies Avec Succès"}
        except:
            dict_response = {"error": True,  "message": "Une Erreur est survenue lors de la Modification des données Fournisseur"}
        return Response(dict_response)

    # queryset = Fournisseur.objects.all()
    # serializer_class = FournisseurSerializer


class BanqueFrsViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        liste_cptes = BanqueFrs.objects.all()
        serializer = BanqueFrsSerializer(liste_cptes, many=True, context = { 'request' : request})
        response_dict = {"error":False, "message":"Liste des Comptes Bancaire Fournisseurs", "data":serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = BanqueFrsSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Compte Bancaire Fornisseur Ajouter Avec Succès"}
        except:
            dict_response = {"error": True, "message": "Une Erreur est survenue lors de l'enregistrement des données Compte de Bancaire du Fournisseur"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = BanqueFrs.objects.all()
        cpte_frs = get_object_or_404(queryset, pk=pk)
        serializer = BanqueFrsSerializer(cpte_frs, context={"request":request})
        return Response({"error":False, "message":"Donnée compte Bancaire", "data":serializer.data})

    def update(self, request, pk=None):
        queryset = BanqueFrs.objects.all()
        cpte_frs = get_object_or_404(queryset, pk=pk)
        serializer = BanqueFrsSerializer(cpte_frs, context={"request": request}, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"error": False, "message": "Compte Bancaire Modifié avec succès", "data": serializer.data})

class FournisseurNameViewset(generics.ListAPIView):
    serializer_class = FournisseurSerializer

    def get_queryset(self):
        nom = self.kwargs["nom"]
        return Fournisseur.objects.filter(nom=nom)

class ProduitViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        liste_produit = Produit.objects.all()
        serializer = ProduitSerializer(liste_produit, many=True, context = { 'request' : request})
        response_dict = {"error":False, "message":"Liste des Produits", "data":serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = ProduitSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Produit Ajouter Avec Succès"}
        except:
            dict_response = {"error": True, "message": "Une Erreur est survenue lors de l'enregistrement du Produit !!"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = Produit.objects.all()
        prod = get_object_or_404(queryset, pk=pk)
        serializer = ProduitSerializer(prod, context={"request":request})
        return Response({"error":False, "message":"Donnée Produit", "data":serializer.data})

    def update(self, request, pk=None):
        queryset = Produit.objects.all()
        prod = get_object_or_404(queryset, pk=pk)
        serializer = ProduitSerializer(prod, context={"request": request}, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"error": False, "message": "Produit Modifié avec succès", "data": serializer.data})


list_fournisseur = FournisseurViewset.as_view({"get":"list"})
create_fournisseur = FournisseurViewset.as_view({"post":"create"})
update_fournisseur = FournisseurViewset.as_view({"post":"update"})


# Create your views here.
