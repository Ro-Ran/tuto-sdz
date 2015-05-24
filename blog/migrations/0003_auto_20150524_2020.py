# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_jeu_date_sortie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('prix', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vendeur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
                ('produits', models.ManyToManyField(related_name='vendeurs', through='blog.Offre', to='blog.Produit')),
            ],
        ),
        migrations.AlterField(
            model_name='voiture',
            name='moteur',
            field=models.OneToOneField(to='blog.Moteur', related_name='voiture'),
        ),
        migrations.AddField(
            model_name='offre',
            name='produit',
            field=models.ForeignKey(to='blog.Produit'),
        ),
        migrations.AddField(
            model_name='offre',
            name='vendeur',
            field=models.ForeignKey(to='blog.Vendeur'),
        ),
    ]
