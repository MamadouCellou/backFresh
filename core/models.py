from django.db import models

class Dispositif(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    mot_de_passe_dispositif = models.CharField(max_length=255)
    cree_a = models.DateTimeField(null=True, blank=True)
    modifie_a = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.id

class Capteur(models.Model):
    id = models.BigAutoField(primary_key=True)
    temperature_frais = models.CharField(max_length=255)
    temperature_sechage = models.CharField(max_length=255, null=True, blank=True)
    humidite_frais = models.CharField(max_length=255, null=True, blank=True)
    humidite_sec = models.CharField(max_length=255, null=True, blank=True)
    dispositifs = models.ForeignKey(Dispositif, on_delete=models.CASCADE)
    cree_a = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Capteur {self.id}"

class CategorieProduit(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    cree_a = models.DateTimeField(null=True, blank=True)
    modifie_a = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nom

class SpecifiqueProduitFrais(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    temp_min = models.IntegerField(null=True, blank=True)
    temp_max = models.IntegerField(null=True, blank=True)
    categorie_produits = models.ForeignKey(CategorieProduit, on_delete=models.CASCADE)
    cree_a = models.DateTimeField(null=True, blank=True)
    modifie_a = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Spécifique Produit Frais {self.nom}"

class ProduitFrais(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    prix_produit = models.FloatField(null=True, blank=True)
    dure_frais = models.IntegerField(null=True, blank=True)
    specifique_produits_frais = models.ForeignKey(SpecifiqueProduitFrais, on_delete=models.CASCADE)
    dispositifs = models.ForeignKey(Dispositif, on_delete=models.CASCADE)
    cree_a = models.DateTimeField()
    modifie_a = models.DateTimeField()

    def __str__(self):
        return f"Produit Frais {self.id}"

class Commande(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    dispositifs = models.ForeignKey(Dispositif, on_delete=models.CASCADE)
    produits_frais = models.ForeignKey(ProduitFrais, on_delete=models.CASCADE)
    cree_a = models.DateTimeField(null=True, blank=True)
    modifie_a = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Commande {self.id}"

class Gps(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    altitude = models.CharField(max_length=255, null=True, blank=True)
    satelitte = models.CharField(max_length=255, null=True, blank=True)
    hdop = models.CharField(max_length=255, null=True, blank=True)
    dispositifs = models.ForeignKey(Dispositif, on_delete=models.CASCADE)
    cree_a = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"GPS {self.id}"

class SpecifiqueProduitSec(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    dure = models.IntegerField(null=True, blank=True)
    categorie_produits = models.ForeignKey(CategorieProduit, on_delete=models.CASCADE)
    cree_a = models.DateTimeField(null=True, blank=True)
    modifie_a = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Spécifique Produit Sec {self.nom}"

class ProduitSec(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    specifique_produits_sec = models.ForeignKey(SpecifiqueProduitSec, on_delete=models.CASCADE)
    dispositifs = models.ForeignKey(Dispositif, on_delete=models.CASCADE)
    cree_a = models.DateTimeField(null=True, blank=True)
    modifie_a = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Produit Sec {self.id}"

from django.db import models

class Utilisateur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=255)
    date_de_naissance = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # Nouveau champ image
    cree_a = models.DateTimeField(null=True, blank=True)
    modifie_a = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.prenom


class UtilisateurDispositif(models.Model):
    id = models.AutoField(primary_key=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    dispositif = models.ForeignKey(Dispositif, on_delete=models.CASCADE)
    cree_a = models.DateTimeField(null=True, blank=True)
    modifie_a = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Utilisateur {self.utilisateur.prenom} - Dispositif {self.dispositif.id}"