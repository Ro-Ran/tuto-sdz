from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

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

def what_is_django(request):
	#Redirige l'utilisateur vers le site de django
	return redirect("https://www.djangoproject.com")

def test_redirect_home(request):
	return redirect(home)

def test_redirect_42(request):
	return redirect('show_article', id_article=42)
