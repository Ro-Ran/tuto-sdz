from django.shortcuts import render, get_object_or_404
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
