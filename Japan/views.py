from django.shortcuts import render
from django.views.generic import View
from .forms import ContactForm
from django.shortcuts import redirect
from .models import ContactInfo
from django.http import JsonResponse

def home_view(request):
    return render(request, 'index.html', {})


def winter_view(request):
    return render(request, 'winterJapan.html', {})


def spring_view(request):
    return render(request, 'springJapan.html', {})


def summer_view(request):
    return render(request, 'summerJapan.html', {})


def autumn_view(request):
    return render(request, 'autumnJapan.html', {})


def signIn_view(request):
    return render(request, 'signIn.html', {})


def signUp_view(request):
    return render(request, 'signUp.html', {})


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact.html', context={'form': form})

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            new_contact = form.save()
            return render(request, 'contact.html', context={'form': form})

class ContactListView(View):
    def get(self, request):
        form = ContactForm()
        contacts = ContactInfo.objects.all()
        return render(request, 'contact_list.html', context={'contacts': contacts})

class ContactDelete(View):
    def post(self, request, id):
        contact = ContactInfo.objects.get(id = id)
        contact.delete()
        return JsonResponse({'result': 'ok'}, status = 200)