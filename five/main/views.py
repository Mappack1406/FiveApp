from multiprocessing import context
from django.shortcuts import render
from django.contrib import messages
from .forms import CustomUserCreationForm, CreateAusstiegAbmulanz, Testdbform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect


from .models import AusstiegAmb, Testdb


def home(request):
    if request.user.is_anonymous:
        return render(request, 'main/index.html')
    item = Testdb.objects.all()
    current_user = User.objects.all().values().get(username=request.user.username)
    context = {'current_user': current_user, 'items': item}
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
def createtest(request):
    if request.method == 'POST':
        f = Testdbform(request.POST, request.user)
        if f.is_valid():
            f.save(user=request.user)
            messages.success(request, 'Post is saved!')
            return redirect('home')
    else:
        current_user = User.objects.all().values().get(username=request.user.username)
        f = Testdbform()
        context = {
            'current_user':current_user, 'form':f
        }
        return render(request, 'main/create.html', context)

@login_required
def updatesurvey(request, id):
    instance = Testdb.objects.get(id=id)

    if request.method == 'POST':
        form = Testdbform(request.POST or None, instance=instance)
        if form.is_valid():
            form.save(user=request.user)
        return redirect('home')
    else:
        form = Testdbform(instance=instance)    
    context = {'venue': instance, 'form': form}
    return render(request, 'main/updatesurvey.html', context)

@login_required
def feed(request):
    user = User.objects.values().get(username=request.user.username)
    survey = AusstiegAmb.objects.all().values()
    context = {'q': survey, 'user': user}
    return render(request, 'main/feed.html', context)