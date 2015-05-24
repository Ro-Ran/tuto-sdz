# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('titre', models.CharField(max_length=100)),
                ('auteur', models.CharField(max_length=42)),
                ('contenu', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Jeu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nom', models.CharField(max_length=25)),
                ('studio', models.CharField(max_length=25)),
                ('date_sortie', models.DateTimeField(verbose_name='Date de sortie', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Moteur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nom', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Personnage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nom', models.CharField(max_length=30)),
                ('jeux', models.ManyToManyField(to='blog.Jeu', related_name='personnages')),
            ],
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nom', models.CharField(max_length=25)),
                ('moteur', models.OneToOneField(to='blog.Moteur')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='categorie',
            field=models.ForeignKey(to='blog.Categorie'),
        ),
    ]
