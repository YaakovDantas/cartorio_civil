from django.contrib import admin
from .models import Nascimento, Casamento, Natimorto, Divorcio, Livro
from django.utils.safestring import mark_safe

# Register your models here.

class AdminLivro(admin.ModelAdmin):
	list_display = ('nome',)

class AdminNascimento(admin.ModelAdmin):
	list_display = ('nome', 'cpf', 'mae','livro', 'ver_imagem') 
	search_fields = ('nome', 'cpf', 'mae','livro__nome')

	def ver_imagem(self, object):
		#return mark_safe('<image src="%s" />' % object.imagem.url)
		return mark_safe('<a href="%s" target="_blank"> Visualizar  </a>' % object.imagem.url)

	ver_imagem.allow_tags = True
	ver_imagem.short_description = 'Imagem'


class AdminCasamento(admin.ModelAdmin):
	list_display = ('marido','mulher', 'cpf_marido', 'cpf_mulher', 'ver_imagem') 
	search_fields = ('marido', 'mulher', 'cpf_marido', 'cpf_mulher')

	def ver_imagem(self, object):
		#return mark_safe('<image src="%s" />' % object.imagem.url)
		return mark_safe('<a href="%s" target="_blank"> Visualizar  </a>' % object.imagem.url)

	ver_imagem.allow_tags = True
	ver_imagem.short_description = 'Imagem'


class AdminNatimorto(admin.ModelAdmin):
	list_display = ('nome', 'cpf', 'mae', 'ver_imagem') 
	search_fields = ('nome', 'cpf', 'mae')

	def ver_imagem(self, object):
		#return mark_safe('<image src="%s" />' % object.imagem.url)
		return mark_safe('<a href="%s" target="_blank"> Visualizar  </a>' % object.imagem.url)

	ver_imagem.allow_tags = True
	ver_imagem.short_description = 'Imagem'


class AdminDivorcio(admin.ModelAdmin):
	list_display = ('marido','mulher', 'cpf_marido', 'cpf_mulher', 'ver_imagem') 
	search_fields = ('marido', 'mulher', 'cpf_marido', 'cpf_mulher')

	def ver_imagem(self, object):
		#return mark_safe('<image src="%s" />' % object.imagem.url)
		return mark_safe('<a href="%s" target="_blank"> Visualizar  </a>' % object.imagem.url)

	ver_imagem.allow_tags = True
	ver_imagem.short_description = 'Imagem'	

admin.site.register(Livro, AdminLivro)
admin.site.register(Nascimento, AdminNascimento)
admin.site.register(Casamento, AdminCasamento)
admin.site.register(Divorcio, AdminDivorcio)
admin.site.register(Natimorto, AdminNatimorto)
