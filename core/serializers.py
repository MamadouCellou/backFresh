import base64

from rest_framework import serializers
from .models import Capteur, CategorieProduit, Commande, Dispositif, Gps, ProduitFrais, ProduitSec, SpecifiqueProduitFrais, SpecifiqueProduitSec, Utilisateur, UtilisateurDispositif


class CapteursSerializer(serializers.ModelSerializer):

    class Meta:
        model = Capteur
        fields = '__all__'


class CategorieProduitSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategorieProduit
        fields = '__all__'


class CommandeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commande
        fields = '__all__'


class DispositifSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dispositif
        fields = '__all__'


class GPSSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gps
        fields = '__all__'


class ProduitsFraisSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProduitFrais
        fields = '__all__'


class ProduitsSecSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProduitSec
        fields = '__all__'


class SpecifiqueProduitFraisSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpecifiqueProduitFrais
        fields = '__all__'


class SpecifiqueProduitSecSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpecifiqueProduitSec
        fields = '__all__'


class UtilisateurSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)  # Assurez-vous que use_url est True

    class Meta:
        model = Utilisateur
        fields = '__all__'


class UtilisateurDispositifSerializer(serializers.ModelSerializer):

    class Meta:
        model = UtilisateurDispositif
        fields = '__all__'
