from multiprocessing import context
from django.shortcuts import render
from django.contrib import messages
from .forms import CustomUserCreationForm, CreateAusstiegAbmulanz
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .decorators import allowed_users


from .models import AusstiegAmb
@login_required
@allowed_users(allowed_roles=['admin', 'customer'])
def deletesurvey(request, id):
    survey = AusstiegAmb.objects.get(id=id)
    survey.delete()
    return redirect('home')

def details(request, id):
    object1 = AusstiegAmb.objects.filter(id=id).values()[0]
    items = AusstiegAmb.objects.get(pk=id)
    context = {'items':items, 'object1':object1}
    return render(request, 'main/details.html', context)

def home(request):
    if request.user.is_anonymous:
        return render(request, 'main/index.html')
    item = AusstiegAmb.objects.all()
    current_user = User.objects.all().values().get(username=request.user.username)
    context = {'current_user': current_user, 'items': item}
    return render(request, 'main/index.html', context)

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
def updatesurvey(request, id):
    survey = AusstiegAmb.objects.get(id=id)
    form = CreateAusstiegAbmulanz(request.POST or None, instance=survey)
    if form.is_valid():
        form.save(user=request.user)
        return redirect('home')
    context = {'survey': survey, 'form': form}
    return render(request, 'main/updatesurvey.html', context)

@login_required
def feed(request):
    user = User.objects.values().get(username=request.user.username)
    survey = AusstiegAmb.objects.all().values()
    context = {'q': survey, 'user': user}
    return render(request, 'main/feed.html', context)