from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Article, Categorie

# Create your views here.
def home (request):
	"""Exemple de page html directement renvoyé par la vue home"""

	articles = Article.objects.all()
	return render (request, 'blog/home.html', {'derniers_articles': articles})

def view_article(request, id_article, slug):
	"""Vue qui prend en paramètre une variable id_article"""

	article = get_object_or_404(Article, id=id_article, slug=slug)

	text = "Vous avez demandé l'article #{0} !".format(id_article)
	return render(request, 'blog/article.html', {'article': article})

def list_articles(request, year, month):
	""" Liste des articles d'un mois précis"""

	text = "Vous avez demandé les articles du {0}/{1}".format(month, year)
	return HttpResponse(text)

def addition(request, nombre1, nombre2):
	total = int(nombre1) + int(nombre2)

	#retourne nombre1, nombre2 et la somme des deux au tpl
	return render(request, 'blog/addition.html', locals())
