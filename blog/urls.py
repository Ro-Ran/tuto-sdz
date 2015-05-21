from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
	url(r'^$', 'home', name="home"),
	url(r'^accueil$', 'home'),
	url(r'^article/(?P<id_article>\d+)$', 'view_article', name="show_article"),
	url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$', 'list_articles', name="list_articles"),
	url(r'^what-is-django$', 'what_is_django', name="django"),
	url(r'^redirect-home$', 'test_redirect_home', name="redirect-home"),
	url(r'^redirect-42$', 'test_redirect_42', name="redirect-42"),
)
