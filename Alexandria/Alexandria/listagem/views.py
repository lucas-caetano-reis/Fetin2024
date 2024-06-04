from django.shortcuts import render, get_object_or_404, redirect
from listagem.models import Livro, Autor
from listagem.forms import LivroFormulario

'''
get_object_or_404 é uma função utilitária fornecida pelo Django. 
Ela é usada para buscar um objeto no banco de dados e retornar uma instância desse objeto se ele for encontrado.
Se o objeto não for encontrado,
em vez de retornar None ou causar um erro que pode não ser tratado adequadamente,
essa função gera automaticamente uma exceção Http404, 
que é convertida em uma resposta HTTP 404 (Página Não Encontrada).
'''

# Create your views here.
def login(request):
    return render(request, 'login.html') #parâmetro request + nome do template

def cadastro(request):
    return render(request, 'cadastro.html')

def menu(request):
    return render(request, 'menu.html')

def listar_livros(request): #função, parâmetro request;
    livros = Livro.objects.all()
    autores = Autor.objects.all()

    context = {"livros":livros , "autores":autores}

    return render(request, 'listagem.html',context) #"livros" = nome pelo qual a variável livros será acessada no template

def livro_info(request, pk): #pk: abreviação de primary key.
    livro = get_object_or_404(Livro, livro_id=pk) #acesso cujo id seja igual a chave primária passada
    return render(request, 'livro_info.html', {'livro': livro})

def adicionarLivro(request):
    if request.method == 'POST':
        formulario = LivroFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/listagem/')
    else:
        formulario = LivroFormulario()
    return render(request, 'livro_form.html', {'formulario':formulario})

def atualizarLivro(request, pk):
    livro = Livro.objects.get(livro_id=pk)

    if request.method == 'POST':
        formulario = LivroFormulario(request.POST, instance=livro)
        if formulario.is_valid():
            formulario.save()
            return redirect('/listagem/')
    else: formulario = LivroFormulario(instance=livro)

    return render(request, 'livro_form.html', {'formulario':formulario})

def removerLivro(request, pk):
    livro = Livro.objects.get(livro_id=pk)

    if request.method == 'POST':
        livro.delete() #remove o livro do banco de dados
        return redirect('/listagem/')
    return render(request, 'delete.html', {'obj':livro})