from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django_registration import signals
from django_registration.backends.one_step.views import RegistrationView
from django_registration.views import RegistrationView as BaseRegistrationView

from accounts.forms import LoginAccountForm
from accounts.models import Profile

User = get_user_model()

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


class CustomRegistrationView(RegistrationView):

    def register(self, form):
        new_user = form.save()
        new_user = authenticate(
            **{
                User.USERNAME_FIELD: new_user.get_username(),
                "password": form.cleaned_data["password1"],
            }
        )
        login(self.request, new_user)

        # Adicionado para request session
        profile = new_user.profiles.get(main_profile=True)
        self.request.session['current-profile'] = profile.id

        signals.user_registered.send(
            sender=self.__class__, user=new_user, request=self.request
        )
        return new_user
