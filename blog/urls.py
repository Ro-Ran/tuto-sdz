from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
	url(r'^$', 'home', name="home"),
	url(r'^accueil$', 'home'),
	url(r'^article/(?P<id_article>\d+)$', 'view_article', name="show_article"),
	url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$', 'list_articles', name="list_articles"),
	url(r'^date$', 'date_actuelle'),
	url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', 'addition'),
)
