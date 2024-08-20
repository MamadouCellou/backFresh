from .models import Capteur, CategorieProduit, Commande, Dispositif, Gps, ProduitFrais, ProduitSec, SpecifiqueProduitFrais, SpecifiqueProduitSec, Utilisateur, UtilisateurDispositif
from rest_framework import viewsets
from .serializers import CapteursSerializer, CommandeSerializer, DispositifSerializer, GPSSerializer, CategorieProduitSerializer, UtilisateurSerializer, UtilisateurDispositifSerializer, SpecifiqueProduitFraisSerializer, SpecifiqueProduitSecSerializer, ProduitsFraisSerializer, ProduitsSecSerializer


class CapteurViewSet(viewsets.ModelViewSet):
    queryset = Capteur.objects.all()
    serializer_class = CapteursSerializer


class CategorieProduitsViewSet(viewsets.ModelViewSet):
    queryset = CategorieProduit.objects.all()
    serializer_class = CategorieProduitSerializer


class SpecifiqueProduitFraisViewSet(viewsets.ModelViewSet):
    queryset = SpecifiqueProduitFrais.objects.all()
    serializer_class = SpecifiqueProduitFraisSerializer

    
class SpecifiqueProduitSecViewSet(viewsets.ModelViewSet):
    queryset = SpecifiqueProduitSec.objects.all()
    serializer_class = SpecifiqueProduitSecSerializer


class ProduitsFraisViewSet(viewsets.ModelViewSet):
    queryset = ProduitFrais.objects.all()
    serializer_class = ProduitsFraisSerializer

    
class ProduitsSecViewSet(viewsets.ModelViewSet):
    queryset = ProduitSec.objects.all()
    serializer_class = ProduitsSecSerializer


class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer


class DispositifViewSet(viewsets.ModelViewSet):
    queryset = Dispositif.objects.all()
    serializer_class = DispositifSerializer


class GPSViewSet(viewsets.ModelViewSet):
    queryset = Gps.objects.all()
    serializer_class = GPSSerializer


class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer


class UtilisateurDispositifViewSet(viewsets.ModelViewSet):
    queryset = UtilisateurDispositif.objects.all()
    serializer_class = UtilisateurDispositifSerializer
