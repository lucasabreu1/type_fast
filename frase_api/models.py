from django.db import models



class Frase(models.Model):
	conteudo = models.CharField(max_length=100)

	def __str__(self):
		return self.conteudo