from django.db import models

class Persona(models.Model):
	nombre = models.TextField(max_length=80)
	apellidos = models.TextField(max_length=100, null=True, blank=True)
	telefono = models.TextField(max_length=20)
	email = models.TextField(max_length=70)
	def __unicode__(self):
		return "%s %s" % (self.nombre, self.apellidos)