from django.contrib import admin
from .models import Dispositif, Capteur, CategorieProduit, SpecifiqueProduitFrais, ProduitFrais, Commande, Gps, SpecifiqueProduitSec, ProduitSec, Utilisateur, UtilisateurDispositif

class DispositifAdmin(admin.ModelAdmin):
    list_display = ['id', 'mot_de_passe_dispositif']
    list_filter = ['id']

class CapteurAdmin(admin.ModelAdmin):
    list_display = ['id', 'temperature_frais', 'cree_a']
    list_filter = ['temperature_frais', 'cree_a']

class CategorieProduitAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom']
    list_filter = ['nom']

class SpecifiqueProduitFraisAdmin(admin.ModelAdmin):
    list_display = ['id', 'temp_min', 'temp_max']
    list_filter = ['temp_min', 'temp_max']

class ProduitFraisAdmin(admin.ModelAdmin):
    list_display = ['id', 'prix_produit', 'dure_frais']
    list_filter = ['prix_produit', 'dure_frais']

class CommandeAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']
    list_filter = ['status']

class GPSAdmin(admin.ModelAdmin):
    list_display = ['id', 'location', 'latitude', 'longitude']
    list_filter = ['location', 'latitude', 'longitude']

class SpecifiqueProduitSecAdmin(admin.ModelAdmin):
    list_display = ['id', 'dure']
    list_filter = ['dure']

class ProduitSecAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']
    list_filter = ['description']

class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'email']
    list_filter = ['nom', 'email']

class UtilisateurDispositifAdmin(admin.ModelAdmin):
    list_display = ['id', 'utilisateur', 'dispositif']
    list_filter = ['utilisateur', 'dispositif']

# Enregistre les classes admin
admin.site.register(Dispositif, DispositifAdmin)
admin.site.register(Capteur, CapteurAdmin)
admin.site.register(CategorieProduit, CategorieProduitAdmin)
admin.site.register(SpecifiqueProduitFrais, SpecifiqueProduitFraisAdmin)
admin.site.register(ProduitFrais, ProduitFraisAdmin)
admin.site.register(Commande, CommandeAdmin)
admin.site.register(Gps, GPSAdmin)
admin.site.register(SpecifiqueProduitSec, SpecifiqueProduitSecAdmin)
admin.site.register(ProduitSec, ProduitSecAdmin)
admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(UtilisateurDispositif, UtilisateurDispositifAdmin)