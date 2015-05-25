# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offre',
            name='produit',
        ),
        migrations.RemoveField(
            model_name='offre',
            name='vendeur',
        ),
        migrations.RemoveField(
            model_name='personnage',
            name='jeux',
        ),
        migrations.RemoveField(
            model_name='vendeur',
            name='produits',
        ),
        migrations.RemoveField(
            model_name='voiture',
            name='moteur',
        ),
        migrations.DeleteModel(
            name='Jeu',
        ),
        migrations.DeleteModel(
            name='Moteur',
        ),
        migrations.DeleteModel(
            name='Offre',
        ),
        migrations.DeleteModel(
            name='Personnage',
        ),
        migrations.DeleteModel(
            name='Produit',
        ),
        migrations.DeleteModel(
            name='Vendeur',
        ),
        migrations.DeleteModel(
            name='Voiture',
        ),
    ]
