from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from listagem.models import Livro
from listagem.forms import LivroFormulario, LivroFiltroFormulario

'''
get_object_or_404 é uma função utilitária fornecida pelo Django. 
Ela é usada para buscar um objeto no banco de dados e retornar uma instância desse objeto se ele for encontrado.
Se o objeto não for encontrado,
em vez de retornar None ou causar um erro que pode não ser tratado adequadamente,
essa função gera automaticamente uma exceção Http404, 
que é convertida em uma resposta HTTP 404 (Página Não Encontrada).
'''

# Create your views here.
def loginPage(request):

    if request.user.is_authenticated:
        return redirect('menu')

    if request.method == 'POST':
        username = request.POST.get('username').lower() #post usuário e deixa ele em minúsculo
        password = request.POST.get('password') #post senha

        try:
            user = User.objects.get(username=username) #verifica se o usuário existe
        except:
            messages.error(request, 'Usuário não existente.') #mostra uma flash message

        user = authenticate(request, username=username, password=password) #autentica o nome de usuário e a senha

        if user is not None: #se o usuário existe
            login(request, user) #cria um sessão no banco de dados
            return redirect('menu') #manda o usuário para o menu
        else:
            messages.error(request, 'Usuário ou senha incorretos.') #mostra uma flash message
    context = {}
    return render(request, 'login.html', context) #parâmetro request + nome do template

def logoutUser(request):
    logout(request) #desloga o usuário
    return redirect('Login') #manda o usuário para a tela de login

def cadastroPage(request):
    if request.user.is_authenticated:
        return redirect('menu')
    
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('menu')
        else:
            messages.error(request,'Um erro ocorreu durante o cadastro')
    
    return render(request, 'cadastro.html', {'form':form})

def menu(request):
    return render(request, 'menu.html')

def listar_livros(request): #função, parâmetro request;
    formularioFiltro = LivroFiltroFormulario(request.GET or None)

    livros = Livro.objects.all()

    if formularioFiltro.is_valid():
        if formularioFiltro.cleaned_data['livro_autor']:
            livros = livros.filter(livro_autor=formularioFiltro.cleaned_data['livro_autor'])
        if formularioFiltro.cleaned_data['livro_serie']:
            livros = livros.filter(livro_serie__icontains=formularioFiltro.cleaned_data['livro_serie'])
        if formularioFiltro.cleaned_data['livro_genero']:
            livros = livros.filter(livro_genero__icontains=formularioFiltro.cleaned_data['livro_genero'])
        if formularioFiltro.cleaned_data['livro_nome']: #Isto é uma pesquisa, não um filtro
            return redirect('Informações do Livro', pk=livros.get(livro_nome__icontains=formularioFiltro.cleaned_data['livro_nome']).pk)

    context = {"livros":livros, "formularioFiltro":formularioFiltro}

    return render(request, 'listagem.html', context) #"livros" = nome pelo qual a variável livros será acessada no template

def livro_info(request, pk): #pk: abreviação de primary key.
    livro = get_object_or_404(Livro, livro_id=pk) #acesso cujo id seja igual a chave primária passada
    return render(request, 'livro_info.html', {'livro': livro})

@login_required(login_url='Login') #caso o usuário não esteja autenticado, ele será redirecionado para a tela de login
def adicionarLivro(request):
    if request.method == 'POST':
        formulario = LivroFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/listagem/')
    else:
        formulario = LivroFormulario()
    return render(request, 'livro_form.html', {'formulario':formulario})

@login_required(login_url='Login') #caso o usuário não esteja autenticado, ele será redirecionado para a tela de login
def atualizarLivro(request, pk):
    livro = Livro.objects.get(livro_id=pk)

    if request.method == 'POST':
        formulario = LivroFormulario(request.POST, instance=livro)
        if formulario.is_valid():
            formulario.save()
            return redirect('/listagem/')
    else: formulario = LivroFormulario(instance=livro)

    return render(request, 'livro_form.html', {'formulario':formulario})

@login_required(login_url='Login') #caso o usuário não esteja autenticado, ele será redirecionado para a tela de login
def removerLivro(request, pk):
    livro = Livro.objects.get(livro_id=pk)

    if request.method == 'POST':
        livro.delete() #remove o livro do banco de dados
        return redirect('/listagem/')
    return render(request, 'delete.html', {'obj':livro})