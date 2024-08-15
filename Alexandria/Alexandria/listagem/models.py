from django.db import models

# Create your models here.
class Autor(models.Model): #tabela dos autores
    autor_id = models.AutoField(primary_key=True) #chave primária do autor
    autor_nome = models.CharField(max_length = 200)

    class Meta:
        ordering = ['autor_nome'] #coloca os autores em ordem de nome

    def __str__(self):
        return self.autor_nome #retorna o atributo nome
    
class Serie(models.Model): #tabela dos livros
    serie_id = models.AutoField(primary_key=True) #chave primária da série
    serie_nome = models.CharField(max_length = 200 , blank = True)

    class Meta:
        ordering = ['serie_nome']

    def __str__(self):
        return self.serie_nome #retorna o atributo nome
    
class Genero(models.Model): #tabela dos livros
    genero_id = models.AutoField(primary_key=True) #chave primária do gênero
    genero_nome = models.CharField(max_length = 200)

    class Meta:
        ordering = ['genero_nome']

    def __str__(self):
        return self.genero_nome #retorna o atributo nome
    
class Livro(models.Model): #tabela dos livros
    livro_id = models.AutoField(primary_key=True) #chave primária do livro
    livro_nome = models.CharField(max_length = 200)
    livro_serie = models.ForeignKey(Serie, models.CASCADE , related_name="serie", blank = True)
    livro_autor = models.ForeignKey(Autor, models.CASCADE, related_name="autor") #relacionamento entre livro e autor: um autor pode escrever vários livros; se um autor for apagado, todos os livros que ele escreveu serão apagados
    livro_genero = models.ForeignKey(Genero, models.CASCADE , related_name="genero")
    livro_sinopse = models.TextField(null = True , blank = True)

    class Meta:
        ordering = ['livro_id']

    def __str__(self):
        return self.livro_nome #retorna o atributo nome