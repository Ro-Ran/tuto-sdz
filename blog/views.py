from django.shortcuts import render, get_object_or_404
from blog.models import Article, Categorie
from blog.forms import ContactForm, ArticleForm

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

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():
			#Ici nous pouvons traiter les données du formulaire
			sujet = form.cleaned_data['sujet']
			message = form.cleaned_data['message']
			envoyeur = form.cleaned_data['envoyeur']
			renvoi = form.cleaned_data['renvoi']

			#envoi de l'email grâce aux données que nous venons de récupérer

			envoi = True
	else:
		form = ContactForm()
	return render(request, 'blog/contact.html', locals())

def add_article(request):
	if request.method == 'POST':
		form = ArticleForm(request.POST)

		if form.is_valid():
			envoi = True
	else:
		form = ArticleForm()
	return render(request, 'blog/add_article.html', locals())

def edit_article(request, id_article):
	if request.method == 'POST':
		form = ArticleForm(request.POST)

		if form.is_valid():
			envoi = True
	else:
		article = get_object_or_404(Article, id=id_article)
		form = ArticleForm(instance=article)
	return render(request, 'blog/add_article.html', locals())
