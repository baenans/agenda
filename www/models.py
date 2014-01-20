from django.db import models

class Persona(models.Model):
	nombre = models.TextField(max_length=80)
	apellidos = models.TextField(max_length=100)
	telefono = models.TextField(max_length=20)
	def __unicode__(self):
		return "%s %s" % (self.nombre, self.apellidos)