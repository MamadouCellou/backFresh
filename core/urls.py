from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CapteurViewSet, CategorieProduitsViewSet, CommandeViewSet, DispositifViewSet, GPSViewSet, ProduitsFraisViewSet, ProduitsSecViewSet, SpecifiqueProduitFraisViewSet, SpecifiqueProduitSecViewSet, UtilisateurViewSet, UtilisateurDispositifViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'capteurs', CapteurViewSet)
router.register(r'categories-produits', CategorieProduitsViewSet)
router.register(r'commandes', CommandeViewSet)
router.register(r'dispositifs', DispositifViewSet)
router.register(r'gps', GPSViewSet)
router.register(r'produits-frais', ProduitsFraisViewSet)
router.register(r'produits-secs', ProduitsSecViewSet)
router.register(r'specifiques-produits-frais', SpecifiqueProduitFraisViewSet)
router.register(r'specifiques-produits-secs', SpecifiqueProduitSecViewSet)
router.register(r'utilisateurs', UtilisateurViewSet)
router.register(r'utilisateurs-dispositifs', UtilisateurDispositifViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
