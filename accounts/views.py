from django.shortcuts import render

from django.contrib.auth import login, logout, authenticate
from accounts.forms import LoginAccountForm
from django.shortcuts import render, redirect
from django.views.generic import ListView
from accounts.models import Profile

def CustomLoginView(request):
    if request.method == 'GET':
        form = LoginAccountForm()
        return render(request, 'registration/login.html', { 'form': form})
    elif request.method == 'POST':
        user = authenticate(request, email=request.POST['email'], password=request.POST['password'])
        if user is None:
            return render(request, 'registration/login.html', { 'form': LoginAccountForm(), 'error': 'Email ou senha incorretos.'})
        else:
            profile = user.profiles.get(main_profile=True)
            login(request, user, backend='accounts.auth.EmailBackend')
            request.session['current-profile'] = profile.id
            return redirect('/')

    return render(request, 'registration/login.html', { 'form': LoginAccountForm() })