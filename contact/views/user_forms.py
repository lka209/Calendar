from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from contact.forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:login')
        else:
            messages.error(request, 'Erro no registro. Verifique os dados.')
    else:
        form = RegisterForm()

    return render(
        request,
        'contact/register.html',
        {'form': form}
    )


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('contact:index')
        else:
            messages.error(request, 'Login inválido')
    else:
        form = AuthenticationForm(request)

    return render(
        request,
        'contact/login.html',
        {'form': form}
    )


def logout_view(request):
    auth.logout(request)
    messages.success(request, 'Você saiu da sessão.')
    return redirect('contact:login')
