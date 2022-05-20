from django.urls import path
from core.views import register, main, groups, news, profile, logout_from
from django.contrib.auth.views import LoginView


urlpatterns = [
    # 1-путь,2-функция,3-кр.название
    path('', main, name='main'),
    path('register/', register, name='register'),
    path('groups/', groups, name='groups'),
    path('news/', news, name='news'),
    path('accounts/profile/', profile, name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_from, name='logout')

]