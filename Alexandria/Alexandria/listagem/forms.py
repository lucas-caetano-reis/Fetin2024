from django.forms import ModelForm
from listagem.models import Livro

class LivroFormulario(ModelForm):
    class Meta:
        model = Livro
        fields = ['livro_id','livro_nome','livro_serie','livro_autor','livro_genero','livro_sinopse']