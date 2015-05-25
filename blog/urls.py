from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
	url(r'^$', 'home', name="home"),
	url(r'^accueil$', 'home'),
	url(r'^article/(?P<id_article>\d+)-(?P<slug>.+)$', 'view_article', name="view"),
	url(r'^contact$', 'contact', name="contact"),
	url(r'^article/create$', 'add_article', name="add-article"),
	url(r'^article/edit/(?P<id_article>\d+)$', 'edit_article', name="edit-article"),
)
