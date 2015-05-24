from django.db import models

# Create your models here.
class Article(models.Model):
	titre = models.CharField(max_length=100)
	auteur = models.CharField(max_length=42)
	contenu = models.TextField(null=True)
	date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")

	categorie = models.ForeignKey('Categorie')

	def __str__(self):
		"""permet de reconnaitre plus facilement les models dans la console python ou l'administration"""
		return self.titre

class Categorie(models.Model):
	nom = models.CharField(max_length=30)

	def __str__(self):
		return self.nom

# example relation OneToOne
class Moteur(models.Model):
	nom = models.CharField(max_length=25)

	def __str__(self):
		return self.nom

class Voiture(models.Model):
	nom = models.CharField(max_length=25)
	#crée la relation ManyToMany avec la classe Moteur : voiture.moteur
	#related_name permet le renomage de la proprièté de navigation inversé
	# par défaut : moteur.voiture_set / avec related_name : jeu.voiture
	moteur = models.OneToOneField(Moteur, related_name='voiture')

	def __str__(self):
		return self.nom

# Example relation ManyToMany simple

class Jeu(models.Model):
	nom = models.CharField(max_length=25)
	studio = models.CharField(max_length=25)

	def __str__(self):
		return self.nom

class Personnage(models.Model):
	nom = models.CharField(max_length=30)

	#crée la relation ManyToMany avec la classe Jeu : perso.jeux.all()
	#related_name permet le renomage de la proprièté de navigation inversé
	# par défaut : jeu.personnage_set.all() / avec related_name : jeu.personnages.all()
	jeux = models.ManyToManyField(Jeu, related_name='personnages')

	def __str__(self):
		return self.nom

# Example relation ManyToMany enrichie

class Produit(models.Model):
	nom = models.CharField(max_length=30)

	def __str__(self):
		return self.nom

class Vendeur(models.Model):
	nom = models.CharField(max_length=30)
	#crée la relation ManyToMany avec la classe Produit : vendeur.produit.all()
	#originalité : through qui permet de definir la table intermediare de la relation ManyToMany
	#Ici cette relation se fait via la classe Offre et peut être enrichie d'autres informations prix par example
	# La relation se crée via la création d'une Offre mais peut ensuite être manipulé comme une relation ManyToMany classique ou presque
	produits = models.ManyToManyField(Produit, related_name='vendeurs', through='Offre')

	def __str__(self):
		return self.nom

class Offre(models.Model):
	prix = models.IntegerField()
	produit = models.ForeignKey(Produit)
	vendeur = models.ForeignKey(Vendeur)

	def __str__(self):
		return "{0} vendu par {1}".format(self.produit, self.vendeur)
