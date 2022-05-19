from django.shortcuts import render
from core.forms import StudentRegistrationForm
from core.forms import Student
from django.contrib.auth.views import auth_logout

def register(request):
    if request.method == 'POST':
        user_form = StudentRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password_1'])
            new_user.save()
            return render(request, 'registration/login.html', {'new_user': new_user})
        else:
            user_form = StudentRegistrationForm()
        return render(request, 'register.html', {'user_form': user_form})
    if request.method == 'GET':
        return render(request, 'register.html')


def main(request):
    return render(request, 'main.html')



def groups(request):
    return render(request, 'groups.html')




def news(request):
    return render(request, 'news.html')



def profile(request):
    return render(request, 'profile.html')

def logout_from(request):
    print('Вышел')
    logout(request)
    return render(request, 'main.html')
