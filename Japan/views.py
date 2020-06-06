from django.shortcuts import render
from django.views.generic import View
from .forms import ContactForm, CreateUserForm, EditProfileForm
from .models import ContactInfo
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='signIn_view')
def home_view(request):
    return render(request, 'index.html', {})


@login_required(login_url='signIn_view')
def winter_view(request):
    return render(request, 'winterJapan.html', {})


@login_required(login_url='signIn_view')
def spring_view(request):
    return render(request, 'springJapan.html', {})


@login_required(login_url='signIn_view')
def summer_view(request):
    return render(request, 'summerJapan.html', {})


@login_required(login_url='signIn_view')
def autumn_view(request):
    return render(request, 'autumnJapan.html', {})


def sign_in_view(request):
    if request.user.is_authenticated:
        return redirect('home_view')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home_view')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, 'signIn.html', context)


def sign_up_view(request):
    if request.user.is_authenticated:
        return redirect('home_view')
    else:
        form = CreateUserForm()
        context = {'form': form}

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'User ' + user + ' was successfully created')
                return redirect('signIn_view')
            else:
                return redirect('signUp_view')

        return render(request, 'signUp.html', context)


@login_required(login_url='signIn_view')
def logout_view(request):
    logout(request)
    return redirect('signIn_view')


@login_required(login_url='login')
def profile_view(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)


@login_required(login_url='login')
def profile_edit_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'profile_edit.html', args)


class ContactView(View):
    @staticmethod
    def get(request):
        form = ContactForm()
        return render(request, 'contact.html', context={'form': form})

    @staticmethod
    def post(request):
        form = ContactForm(request.POST)

        if form.is_valid():
            return render(request, 'contact.html', context={'form': form})


class ContactListView(View):
    @staticmethod
    def get(request):
        contacts = ContactInfo.objects.all()
        return render(request, 'contact_list.html', context={'contacts': contacts})


class ContactDelete(View):
    @staticmethod
    def post(request, ide):
        contact = ContactInfo.objects.get(id=ide)
        contact.delete()
        return JsonResponse({'result': 'ok'}, status=200)
