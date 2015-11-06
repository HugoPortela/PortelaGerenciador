from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login, logout
from django.http import HttpResponse

from .forms import UserForm, UserProfileForm,ProdutosForm
from .models import ProdutoProfiles

# Create your views here.

def home (request):
    produtos = ProdutoProfiles.objects.all()
    return render(request, 'base.html',{'produtos' : produtos})

def cadastro_usuario(request):
    if request.method == 'POST':
            user_form = UserForm(request.POST)
            profile_form = UserProfileForm(request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                        user = user_form.save()
                        user.set_password(user.password)
                        user.save()
                        profile = profile_form.save(commit=False)
                        profile.user = user

                        if 'foto' in request.FILES:
                                profile.foto = request.FILES['foto']

                        profile.save()
                        return redirect('core:usuariosucesso')
            else:
                        print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'core/cadastro_usuario.html',\
        {'user_form': user_form, 'profile_form': profile_form})

def sucesso_usuario(request):
    return render(request, 'core/sucesso_usuario.html')

def sucesso_produto(request):
    return render(request, 'core/sucesso_produto.html')

def cadastro_produtos(request):
    if request.method == 'POST':
        produto_form = ProdutosForm(request.POST)
        if produto_form.is_valid():
                produto_form.save()
                return redirect('core:sucessoproduto')
        else:
                print(produto_form.errors)
    else:
        produto_form=ProdutosForm()

    return render (request, 'core/cadastro_produto.html', {'produto_form': produto_form})



#def listar_produtos(request):
    #produtos = ProdutoProfiles.objects.all()
    #return render(request, 'base.html',{'produtos' : produtos})