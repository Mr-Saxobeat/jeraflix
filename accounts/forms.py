from django_registration.forms import RegistrationForm
from accounts.models import CustomAccount

class AccountForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = CustomAccount