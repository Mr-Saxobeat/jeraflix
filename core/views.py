from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from accounts.forms import LoginAccountForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


class IndexTemplateView(LoginRequiredMixin, TemplateView):

    def get_template_names(self):
        template_name = 'index.html'
        return template_name

def CustomLoginView(request):
    if request.method == 'GET':
        form = LoginAccountForm()
        return render(request, 'registration/login.html', { 'form': form})
    elif request.method == 'POST':
        print(request.POST['email'])
        print(request.POST['password'])
        user = authenticate(request, email=request.POST['email'], password=request.POST['password'])
        if user is None:
            print('deu rum')
            return render(request, 'registration/login.html', { 'form': LoginAccountForm(), 'error': 'Email ou senha incorretos.'})
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'registration/login.html', { 'form': form })
