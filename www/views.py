from django.shortcuts import render
from www.models import Persona
from django import forms

# Create your views here.

class Formulario(forms.ModelForm):
	class Meta:
		model = Persona

def home(request):
	if request.method == 'POST': 
		formulario = Formulario(request.POST)
		if formulario.is_valid():
			formulario.save()
			return redirect('home')

	else:
		formulario = Formulario()
		context = {	'personas' : Persona.objects.all(),
					'formulario': formulario }
		return render(request, 'home.htm', context)