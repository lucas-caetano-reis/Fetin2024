from django.forms import ModelForm
from django import forms
from listagem.models import Livro, Autor

class LivroFormulario(ModelForm):
    class Meta:
        model = Livro
        fields = ['livro_id','livro_nome','livro_serie','livro_autor','livro_genero','livro_sinopse']

class LivroFiltroFormulario(forms.Form):
    livro_autor = forms.ModelChoiceField(queryset=Autor.objects.all(), required=False, label='Autor')
    livro_serie = forms.CharField(max_length=200, required=False, label='Série')
    livro_genero = forms.CharField(max_length=100, required=False, label='Gênero')
    livro_nome = forms.CharField(max_length=200, required=False, label='Nome do Livro')

'''
class LivroFiltroFormulario(ModelForm):
    class Meta:
        model = Livro
        fields = ['livro_nome','livro_serie','livro_autor','livro_genero']
'''