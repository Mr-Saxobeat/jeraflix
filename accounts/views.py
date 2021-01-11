from django.shortcuts import render

from django.contrib.auth import login, logout, authenticate
from accounts.forms import LoginAccountForm
from django.shortcuts import render, redirect

def CustomLoginView(request):
    if request.method == 'GET':
        form = LoginAccountForm()
        return render(request, 'registration/login.html', { 'form': form})
    elif request.method == 'POST':
        user = authenticate(request, email=request.POST['email'], password=request.POST['password'])
        if user is None:
            return render(request, 'registration/login.html', { 'form': LoginAccountForm(), 'error': 'Email ou senha incorretos.'})
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'registration/login.html', { 'form': form })

