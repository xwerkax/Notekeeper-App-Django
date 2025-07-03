# Django Notes App

⚠️ **Work in Progress** - This application is currently under development

## Current Status

- [x] Basic Django setup
- [x] Admin login functionality
- [x] Adding notes
- [x] Editing notes
- [x] Note deletion 
- [x] Note filtering
- [x] Basic interface

## Planned Features

- [ ] AI-powered note summarization - Automatic summarization of long notes using AI
- [ ] Modern UI/UX design - Clean and intuitive user interface
- [ ] User registration & authentication - Full user management system
- [ ] Categories and tags - Organize notes with categories and tagging system
- [ ] Export functionality - Export notes to various formats (PDF, TXT, etc.)

## Tech Stack

- Django
- Python
- SQLite (development)
- HTML/CSS
- JavaScript

## Instalacja

1. Sklonuj repozytorium:

- bashgit clone [url-repozytorium]
- cd projekt-notatki

2. Utwórz wirtualne środowisko:

- bashpython -m venv venv
- source venv/bin/activate  # Linux/Mac
# lub
- venv\Scripts\activate  # Windows

3. Zainstaluj zależności:

- bashpip install -r requirements.txt

4. Wykonaj migracje:

- bashpython manage.py makemigrations
- python manage.py migrate

5. Utwórz superusera (opcjonalnie):

- bashpython manage.py createsuperuser

6. Uruchom serwer:

- bashpython manage.py runserver

  ## Wymagania
- Python 3.8+
- Django 4.0+
- Baza danych (SQLite domyślnie)
