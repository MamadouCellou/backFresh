from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import (
    Capteur, CategorieProduit, Commande, Dispositif, Gps,
    ProduitFrais, ProduitSec, SpecifiqueProduitFrais,
    SpecifiqueProduitSec, Utilisateur, UtilisateurDispositif
)
from rest_framework import viewsets
from .serializers import (
    CapteursSerializer, CommandeSerializer, DispositifSerializer,
    GPSSerializer, CategorieProduitSerializer, UtilisateurSerializer,
    UtilisateurDispositifSerializer, SpecifiqueProduitFraisSerializer,
    SpecifiqueProduitSecSerializer, ProduitsFraisSerializer, ProduitsSecSerializer
)


class CapteurViewSet(viewsets.ModelViewSet):
    queryset = Capteur.objects.all()
    serializer_class = CapteursSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'temperature_frais', 'temperature_sechage', 'humidite_frais', 'humidite_sec', 'dispositifs', 'cree_a']
    search_fields = ['temperature_frais', 'temperature_sechage', 'humidite_frais', 'humidite_sec']
    ordering_fields = ['id', 'temperature_frais', 'temperature_sechage', 'humidite_frais', 'humidite_sec', 'cree_a']


class CategorieProduitsViewSet(viewsets.ModelViewSet):
    queryset = CategorieProduit.objects.all()
    serializer_class = CategorieProduitSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'nom', 'cree_a', 'modifie_a']
    search_fields = ['nom']
    ordering_fields = ['id', 'nom', 'cree_a', 'modifie_a']


class SpecifiqueProduitFraisViewSet(viewsets.ModelViewSet):
    queryset = SpecifiqueProduitFrais.objects.all()
    serializer_class = SpecifiqueProduitFraisSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'nom', 'temp_min', 'temp_max', 'categorie_produits', 'cree_a', 'modifie_a']
    search_fields = ['nom']
    ordering_fields = ['id', 'nom', 'temp_min', 'temp_max', 'cree_a', 'modifie_a']


class SpecifiqueProduitSecViewSet(viewsets.ModelViewSet):
    queryset = SpecifiqueProduitSec.objects.all()
    serializer_class = SpecifiqueProduitSecSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'nom', 'dure', 'categorie_produits', 'cree_a', 'modifie_a']
    search_fields = ['nom']
    ordering_fields = ['id', 'nom', 'dure', 'cree_a', 'modifie_a']


class ProduitsFraisViewSet(viewsets.ModelViewSet):
    queryset = ProduitFrais.objects.all()
    serializer_class = ProduitsFraisSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'description', 'prix_produit', 'dure_frais', 'specifique_produits_frais', 'dispositifs', 'cree_a', 'modifie_a']
    search_fields = ['description']
    ordering_fields = ['id', 'description', 'prix_produit', 'dure_frais', 'cree_a', 'modifie_a']


class ProduitsSecViewSet(viewsets.ModelViewSet):
    queryset = ProduitSec.objects.all()
    serializer_class = ProduitsSecSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'description', 'specifique_produits_sec', 'dispositifs', 'cree_a', 'modifie_a']
    search_fields = ['description']
    ordering_fields = ['id', 'description', 'cree_a', 'modifie_a']


class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'status', 'dispositifs', 'produits_frais', 'cree_a', 'modifie_a']
    search_fields = ['status']
    ordering_fields = ['id', 'status', 'cree_a', 'modifie_a']


class DispositifViewSet(viewsets.ModelViewSet):
    queryset = Dispositif.objects.all()
    serializer_class = DispositifSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'mot_de_passe_dispositif', 'cree_a', 'modifie_a']
    search_fields = ['id', 'mot_de_passe_dispositif']
    ordering_fields = ['id', 'mot_de_passe_dispositif', 'cree_a', 'modifie_a']


class GPSViewSet(viewsets.ModelViewSet):
    queryset = Gps.objects.all()
    serializer_class = GPSSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'location', 'latitude', 'longitude', 'altitude', 'satelitte', 'hdop', 'dispositifs', 'cree_a']
    search_fields = ['location', 'latitude', 'longitude', 'altitude']
    ordering_fields = ['id', 'location', 'latitude', 'longitude', 'altitude', 'satelitte', 'hdop', 'cree_a']


class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'nom', 'prenom', 'profession', 'email', 'date_de_naissance', 'cree_a', 'modifie_a']
    search_fields = ['nom', 'prenom', 'profession', 'email']
    ordering_fields = ['id', 'nom', 'prenom', 'profession', 'email', 'date_de_naissance', 'cree_a', 'modifie_a']


class UtilisateurDispositifViewSet(viewsets.ModelViewSet):
    queryset = UtilisateurDispositif.objects.all()
    serializer_class = UtilisateurDispositifSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'utilisateur', 'dispositif', 'cree_a', 'modifie_a']
    search_fields = ['utilisateur__prenom', 'dispositif__id']
    ordering_fields = ['id', 'utilisateur', 'dispositif', 'cree_a', 'modifie_a']
