from multiprocessing import context
from django.shortcuts import render
from django.contrib import messages
from .forms import CustomUserCreationForm, CreateAusstiegAbmulanz
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect


from .models import AusstiegAmb


def home(request):
    if request.user.is_anonymous:
        return render(request, 'main/index.html')
    current_user = User.objects.all().values().get(username=request.user.username)
    context = {'current_user': current_user}
    return render(request, 'main/index.html', context)

@login_required
def profile(request, user_username):
    current_user = User.objects.all().values().get(username=request.user.username)
    if user_username != current_user['username']:
        external_user = User.objects.all().values().get(username=user_username)
        context = {'external_user': external_user}
        return render(request, 'main/index.html', context)
    context = {'current_user': current_user}
    return render(request,"main/index.html", context)

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')

            return redirect('register')
        else:
            messages.error(request, 'Failed')
            return redirect('register')
    else:
        f = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form':f})

@login_required
def create(request):
    if request.method == 'POST':
            f = CreateAusstiegAbmulanz(request.POST, request.user)
            if f.is_valid():
                f.save(user=request.user)
                messages.success(request, 'Post is saved!')
                return redirect('home')
    else:
        current_user = User.objects.all().values().get(username=request.user.username)
        f = CreateAusstiegAbmulanz()
        context = {
            'current_user':current_user, 'form':f
        }
        return render(request, 'main/create.html', context)

@login_required
def feed(request):
    user = User.objects.values().get(username=request.user.username)
    survey = AusstiegAmb.objects.all().values()
    context = {'q': survey, 'user': user}
    return render(request, 'main/feed.html', context)