from django.forms import ModelForm
from django.forms import CharField, PasswordInput
from .models import Student


class StudentRegistrationForm(ModelForm):

    password_1 = CharField(max_length=20, min_length=6, widget=PasswordInput)
    password_2 = CharField(max_length=20, min_length=6, widget=PasswordInput)

    class Meta:
        model = Student
        fields = ( 'first_name', 'last_name', 'username', 'age')

    def check_pass(self):
        data = self.cleaned_data
        if data['password_1'] != data['password_2']:
            raise ValidationError('Неверный повтор пароля')
        return data['password_1']