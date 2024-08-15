from django.contrib import admin

# Register your models here.
from listagem.models import Autor, Livro, Serie, Genero

class AutorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nome do autor', {'fields': ['autor_nome']}),
    ]

class SerieAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nome da série', {'fields': ['serie_nome']}),
    ]

class GeneroAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nome do gênero', {'fields': ['genero_nome']}),
    ]

class LivroAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nome do livro', {'fields': ['livro_nome']}),
        ('Série a qual o livro pertence', {'fields': ['livro_serie']}),
        ('Autor do livro', {'fields': ['livro_autor']}),
        ('Gênero do livro', {'fields': ['livro_genero']}),
        ('Sinopse do livro', {'fields': ['livro_sinopse'], 'classes': ['collapse']}),
    ]
    list_display = ('livro_nome', 'livro_serie', 'livro_autor', 'livro_genero')
    list_filter = ['livro_autor', 'livro_genero', 'livro_serie']
    search_fields = ['livro_nome']

admin.site.register(Autor, AutorAdmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Genero, GeneroAdmin)