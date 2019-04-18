from django.db import models
from bet_project.settings import BASE_DIR
from django.utils.html import format_html
# Create your models here.
class Livro(models.Model):
	nome = models.CharField(max_length=255, null=False)

	def __str__(self):
		return self.nome

class Nascimento(models.Model):
	livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
	nome = models.CharField(max_length=255, null=False)
	cpf = models.CharField(max_length=15, null=False)
	pai = models.CharField(max_length=255, null=False)
	mae = models.CharField(max_length=255, null=False)
	imagem = models.ImageField(upload_to="fotos", null=False)

class Casamento(models.Model):
	livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
	marido = models.CharField(max_length=255, null=False)
	mulher = models.CharField(max_length=255, null=False)
	cpf_marido = models.CharField(max_length=15, null=False)
	cpf_mulher = models.CharField(max_length=15, null=False)
	imagem = models.ImageField(upload_to="fotos", null=False)


class Natimorto(models.Model):
	livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
	nome = models.CharField(max_length=255, null=False)
	cpf = models.CharField(max_length=15, null=False)
	pai = models.CharField(max_length=255, null=False)
	mae = models.CharField(max_length=255, null=False)
	imagem = models.ImageField(upload_to="fotos", null=False)

class Divorcio(models.Model):
	livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
	marido = models.CharField(max_length=255, null=False)
	mulher = models.CharField(max_length=255, null=False)
	cpf_marido = models.CharField(max_length=15, null=False)
	cpf_mulher = models.CharField(max_length=15, null=False)
	imagem = models.ImageField(upload_to="fotos", null=False)
		