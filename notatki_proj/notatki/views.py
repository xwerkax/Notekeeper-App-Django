from django.shortcuts import render, redirect
from .models import Notatka
from .forms import NotatkaForm

def lista_notatek(request):
    notatki = Notatka.objects.all().order_by('data')
    return render(request, 'notatki/lista.html', {'notatki': notatki})

def dodaj_notatke(request):
    if request.method == "POST":
        form = NotatkaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notatek')  # musisz mieć taki widok/URL
    else:
        form = NotatkaForm()
    return render(request, 'notatki/formularz.html', {'form': form})