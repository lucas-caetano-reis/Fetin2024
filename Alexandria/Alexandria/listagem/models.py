from django.db import models

# Create your models here.
class Autor(models.Model): #tabela dos autores
    autor_id = models.AutoField(primary_key=True) #chave primária do autor
    autor_nome = models.CharField(max_length = 200)

    class Meta:
        ordering = ['autor_nome'] #coloca os autores em ordem de nome

    def __str__(self):
        return self.autor_nome #retorna o atributo nome

class Livro(models.Model): #tabela dos livros
    livro_id = models.AutoField(primary_key=True) #chave primária do livro
    livro_nome = models.CharField(max_length = 200)
    livro_serie = models.CharField(max_length = 200 , null = True , blank = True) #blank: permite texto vazio
    livro_autor = models.ForeignKey(Autor, models.CASCADE, related_name="autor") #relacionamento entre livro e autor: um autor pode escrever vários livros; se um autor for apagado, todos os livros que ele escreveu serão apagados
    livro_genero = models.CharField(max_length = 200)
    livro_sinopse = models.TextField(null = True , blank = True)

    class Meta:
        ordering = ['livro_id']

    def __str__(self):
        return self.livro_nome #retorna o atributo nome