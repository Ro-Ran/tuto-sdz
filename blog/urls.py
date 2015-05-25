from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
	url(r'^$', 'home', name="home"),
	url(r'^accueil$', 'home'),
	url(r'^article/(?P<id_article>\d+)-(?P<slug>.+)$', 'view_article', name="view"),
)
