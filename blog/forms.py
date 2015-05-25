from django import forms
from blog.models import Article

class ContactForm(forms.Form):
	sujet = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	envoyeur = forms.EmailField(label="Votre adresse mail")
	renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie envoyé", required=False)

	#Validation custom du champ message
	# def clean_message(self):
	# 	message = self.cleaned_data['message']
	# 	if "call of duty" in message:
	# 		raise forms.ValidationError("On parle pas pas de néant vidéoludique ici !")
	# 	return message

	#Validation custom sur plusieurs champs
	def clean(self):
		cleaned_data = super(ContactForm, self).clean()
		sujet = cleaned_data.get('sujet').lower()
		message = cleaned_data.get('message').lower()

		if sujet and message:
			if "call of" in sujet and "call of" in message:
				msg = "Vous parlez de call of duty dans le sujet ET le message ? Non mais ho !"
				self.add_error("message", msg)

		return cleaned_data

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		#ajoute tous les champs du model Article
		fields = '__all__'
		#exclus le champ auteur
		#exclude = ('auteur',)
		#utilise seulement titre et message
		#fields = ('titre', 'contenu',)
