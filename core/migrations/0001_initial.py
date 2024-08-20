# Generated by Django 5.1 on 2024-08-19 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategorieProduit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=255, null=True)),
                ('cree_a', models.DateTimeField(blank=True, null=True)),
                ('modifie_a', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dispositif',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('mot_de_passe_dispositif', models.CharField(max_length=255)),
                ('cree_a', models.DateTimeField(blank=True, null=True)),
                ('modifie_a', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('profession', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mot_de_passe', models.CharField(max_length=255)),
                ('date_de_naissance', models.DateField(blank=True, null=True)),
                ('cree_a', models.DateTimeField(blank=True, null=True)),
                ('modifie_a', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Capteur',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('temperature_frais', models.CharField(max_length=255)),
                ('temperature_sechage', models.CharField(blank=True, max_length=255, null=True)),
                ('humidite_frais', models.CharField(blank=True, max_length=255, null=True)),
                ('humidite_sec', models.CharField(blank=True, max_length=255, null=True)),
                ('cree_a', models.DateTimeField(blank=True, null=True)),
                ('dispositifs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dispositif')),
            ],
        ),
        migrations.CreateModel(
            name='Gps',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('altitude', models.CharField(blank=True, max_length=255, null=True)),
                ('satelitte', models.CharField(blank=True, max_length=255, null=True)),
                ('hdop', models.CharField(blank=True, max_length=255, null=True)),
                ('cree_a', models.DateTimeField(blank=True, null=True)),
                ('dispositifs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dispositif')),
            ],
        ),
        migrations.CreateModel(
            name='ProduitFrais',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('prix_produit', models.FloatField(blank=True, null=True)),
                ('dure_frais', models.IntegerField(blank=True, null=True)),
                ('cree_a', models.DateTimeField()),
                ('modifie_a', models.DateTimeField()),
                ('dispositifs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dispositif')),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('cree_a', models.DateTimeField(blank=True, null=True)),
                ('modifie_a', models.DateTimeField(blank=True, null=True)),
                ('dispositifs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dispositif')),
                ('produits_frais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.produitfrais')),
            ],
        ),
        migrations.CreateModel(
            name='SpecifiqueProduitFrais',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=255, null=True)),
                ('temp_min', models.IntegerField(blank=True, null=True)),
                ('temp_max', models.IntegerField(blank=True, null=True)),
                ('cree_a', models.DateTimeField(blank=True, null=True)),
                ('modifie_a', models.DateTimeField(blank=True, null=True)),
                ('categorie_produits', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categorieproduit')),
            ],
        ),
        migrations.AddField(
            model_name='produitfrais',
            name='specifique_produits_frais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.specifiqueproduitfrais'),
        ),
        migrations.CreateModel(
            name='SpecifiqueProduitSec',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=255, null=True)),
                ('dure', models.IntegerField(blank=True, null=True)),
                ('cree_a', models.DateTimeField(blank=True, null=True)),
                ('modifie_a', models.DateTimeField(blank=True, null=True)),
                ('categorie_produits', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categorieproduit')),
            ],
        ),
        migrations.CreateModel(
            name='ProduitSec',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('cree_a', models.DateTimeField(blank=True, null=True)),
                ('modifie_a', models.DateTimeField(blank=True, null=True)),
                ('dispositifs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dispositif')),
                ('specifique_produits_sec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.specifiqueproduitsec')),
            ],
        ),
        migrations.CreateModel(
            name='UtilisateurDispositif',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cree_a', models.DateTimeField(blank=True, null=True)),
                ('modifie_a', models.DateTimeField(blank=True, null=True)),
                ('dispositif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dispositif')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.utilisateur')),
            ],
        ),
    ]
