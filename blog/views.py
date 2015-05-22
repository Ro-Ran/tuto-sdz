from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime

# Create your views here.
def home (request):
	"""Exemple de page html directement renvoyé par la vue home"""

	text = """<h1>Bienvenue sur le blog tuto-sdz</h1>
		<p>The cake is a lie...</p>"""
	return HttpResponse(text)

def view_article(request, id_article):
	"""Vue qui prend en paramètre une variable id_article"""

	#Si l'id est inférieur à 1, nous considerons que l'article n'existe pas
	if int(id_article) < 1:
		raise Http404

	text = "Vous avez demandé l'article #{0} !".format(id_article)
	return HttpResponse(text)

def list_articles(request, year, month):
	""" Liste des articles d'un mois précis"""

	text = "Vous avez demandé les articles du {0}/{1}".format(month, year)
	return HttpResponse(text)

def date_actuelle(request):
	return render(request, 'blog/date.html', {'date': datetime.now()})

def addition(request, nombre1, nombre2):
	total = int(nombre1) + int(nombre2)

	#retourne nombre1, nombre2 et la somme des deux au tpl
	return render(request, 'blog/addition.html', locals())
