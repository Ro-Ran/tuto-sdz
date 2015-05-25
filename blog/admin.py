from django.contrib import admin
from blog.models import Article, Categorie

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('titre', 'auteur', 'date', 'apercu_contenu',)
	list_filter = ('auteur', 'categorie',)
	date_hierarchy = 'date'
	ordering = ('date',)
	search_fields = ('titre', 'contenu')
	prepopulated_fields = {"slug": ("titre",),}

	fieldsets = (
		# Fieldset 1 : meta-info (titre,auteur...)
		('Général', {
			'classes': ['extrapretty',],
			'fields': ('titre', 'slug', 'auteur', 'categorie'),
		}),
		('Contenu de l\'article', {
			'description': 'le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
			'fields': ('contenu',)
		})
	)

	def apercu_contenu(self, article):
		"""
		Retourne les 40 premiers caractères du contenu de l'article. S'il
		y a plus de 40 caractères, il faut ajouter des points de suspension.
		"""
		text = article.contenu[0:40]
		if len(article.contenu) > 40:
			return '%s...' % text
		else:
			return text

	#Entete de notre colonne
	apercu_contenu.short_description = 'Aperçu du contenu'

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
