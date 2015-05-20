from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
	"""Exemple de page html directement renvoyé par la vue home"""

	text = """<h1>Bienvenue sur le blog tuto-sdz</h1>
		<p>The cake is a lie...</p>"""
	return HttpResponse(text)
