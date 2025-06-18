from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Notatka
from django.contrib import messages
def lista_notatek(request):
    notatki = Notatka.objects.all().order_by('data')
    return render(request, 'notatki/lista.html', {'notatki': notatki})


@login_required
def dodaj_notatke(request):
    if request.method == 'POST':
        notatka = Notatka()
        notatka.tytul = request.POST.get('tytul')
        notatka.przedmiot = request.POST.get('przedmiot')
        notatka.data = request.POST.get('data')
        notatka.tresc = request.POST.get('tresc')
        notatka.autor = request.user  # ← DODAJ TO!
        notatka.save()

        return redirect('lista_notatek')

    return render(request, 'notatki/formularz.html')


@login_required
def edytuj_notatke(request, notatka_id):
    notatka = get_object_or_404(Notatka, id=notatka_id, autor=request.user)

    # Pobierz unikalne przedmioty użytkownika
    przedmioty = Notatka.objects.filter(
        autor=request.user,
        przedmiot__isnull=False
    ).exclude(przedmiot='').values_list('przedmiot', flat=True).distinct()

    # OBSŁUGA ZAPISYWANIA ZMIAN
    if request.method == 'POST':
        # Pobierz dane z formularza
        notatka.tytul = request.POST.get('tytul')
        notatka.data = request.POST.get('data')
        notatka.tresc = request.POST.get('tresc')

        # Obsługa przedmiotu (zwykły lub nowy)
        przedmiot = request.POST.get('przedmiot')
        if przedmiot == 'nowy':
            notatka.przedmiot = request.POST.get('nowy_przedmiot')
        else:
            notatka.przedmiot = przedmiot

        # Zapisz zmiany
        notatka.save()

        # Przekieruj do listy notatek
        return redirect('moje_notatki')

    # JEŚLI GET - pokaż formularz
    context = {
        'notatka': notatka,
        'przedmioty': przedmioty,
    }
    return render(request, 'notatki/edytuj_notatke.html', context)

@login_required
def moje_notatki(request):
    # Pobierz notatki tego użytkownika
    notatki = Notatka.objects.filter(
        autor=request.user
    ).order_by('-data')

    # Policz notatki
    liczba_notatek = notatki.count()

    # Pobierz przedmioty dla filtrów
    przedmioty = Notatka.objects.filter(
        autor=request.user,
        przedmiot__isnull=False
    ).exclude(przedmiot='').values_list('przedmiot', flat=True).distinct()

    context = {
        'notatki': notatki,
        'liczba_notatek': liczba_notatek,
        'przedmioty': przedmioty,
    }

    return render(request, 'notatki/moje_notatki.html', context)


@login_required
def usun_notatke(request, notatka_id):
    # Pobierz notatkę TYLKO jeśli należy do tego użytkownika
    notatka = get_object_or_404(Notatka, id=notatka_id, autor=request.user)
    tytul = notatka.tytul

    # Usuń z bazy danych
    notatka.delete()
    messages.success(request, f'Notatka"{tytul}" została usunięta.')
    # Przekieruj z powrotem do listy notatek
    return redirect('moje_notatki')

@login_required
def podglad_notatki(request, notatka_id):
    notatka = get_object_or_404(Notatka, id=notatka_id, autor=request.user)

    context = {'notatka': notatka}
    return render(request, 'notatki/podglad_notatki.html', context)

