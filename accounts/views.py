from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.views import View
from .models import Profile








def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username = data['username'],
                                password = data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Siz tizimga login qildingiz! ')
                else:
                    return HttpResponse('Siz profilingiz tizimda faol holatda emas😥')

            else:
                return HttpResponse('Login parolda xatolik bor🤬')

    else:
        form = LoginForm()
        context = {
            'form' : form,
        }
    return render(request, 'registration/login.html', context)





def dashboard_view(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    context = {
        'user':user,
        'profile': profile,
    }
    return render(request, 'pages/user_profile.html', context)