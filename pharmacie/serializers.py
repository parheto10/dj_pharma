from rest_framework import serializers

from .models import (
    Fournisseur,
    BanqueFrs,
    Produit,
    DetailProd,
    Employer,
    Client,
    Facture,
    RequeteClt,
    CompteFournisseur,
    BanqueFrs, BanqueEmp
)


class FournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fournisseur
        fields = "__all__"

class BanqueFrsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BanqueFrs
        fields = "__all__"

    # appel de la cle etranger[Fournisseur]
    def to_representation(self, instance):
        #response = super(BanqueFrsSerializer, self).to_representation()
        response = super().to_representation(instance)
        response['infos fournisseur'] = FournisseurSerializer(instance.fournisseur_id).data
        return response


class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = "__all__"
    #appel de la cle etranger[Fournisseur]
    def to_representation(self, instance):
        #response = super(BanqueFrsSerializer, self).to_representation()
        response = super().to_representation(instance)
        response['fournisseur'] = FournisseurSerializer(instance.fournisseur_id).data
        return response

class DetailProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailProd
        fields = "__all__"
    # appel de la cle etranger[Produit]
    def to_representation(self, instance):
        # response = super(BanqueFrsSerializer, self).to_representation()
        response = super().to_representation(instance)
        response['produit'] = ProduitSerializer(instance.produit_id).data
        return response

class DetailProdSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = DetailProd
        fields = "__all__"

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = "__all__"
    # appel de la cle etranger[Produit]
    def to_representation(self, instance):
        # response = super(BanqueFrsSerializer, self).to_representation()
        response = super().to_representation(instance)
        response['client'] = ClientSerializer(instance.client_id).data
        return response

class RequeteCltSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequeteClt
        fields = "__all__"
    # appel de la cle etranger[Client]
    def to_representation(self, instance):
        # response = super(BanqueFrsSerializer, self).to_representation()
        response = super().to_representation(instance)
        response['client'] = ClientSerializer(instance.client_id).data
        return response

    # appel de la cle etranger[Produit]
    def to_representation(self, instance):
        # response = super(BanqueFrsSerializer, self).to_representation()
        response = super().to_representation(instance)
        response['produit'] = ProduitSerializer(instance.produit_id).data
        return response

class CompteFournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompteFournisseur
        fields = "__all__"
    # appel de la cle etranger[Produit]
    def to_representation(self, instance):
        # response = super(BanqueFrsSerializer, self).to_representation()
        response = super().to_representation(instance)
        response['fournisseur'] = FournisseurSerializer(instance.fournisseur_id).data
        return response

class BanqueFrsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BanqueFrs
        fields = "__all__"
    # appel de la cle etranger[Produit]
    def to_representation(self, instance):
        # response = super(BanqueFrsSerializer, self).to_representation()
        response = super().to_representation(instance)
        response['fournisseur'] = FournisseurSerializer(instance.fournisseur_id).data
        return response

class BanqueEmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = BanqueEmp
        fields = "__all__"
    # appel de la cle etranger[Produit]
    def to_representation(self, instance):
        # response = super(BanqueFrsSerializer, self).to_representation()
        response = super().to_representation(instance)
        response['employer'] = EmployerSerializer(instance.emplyer_id).data
        return response