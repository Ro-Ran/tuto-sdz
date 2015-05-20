from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
	url(r'^$', 'home'),
	url(r'^accueil$', 'home'),
)
