#Sklonuj repozytorium na swój lokalny komputer:

git clone <URL_repozytorium>

#Utwórz wirtualne środowisko Pythona:

python3 -m venv venv

#Aktywuj wirtualne środowisko:
source venv/bin/activate

#Zainstaluj wymagane pakiety Pythona z pliku requirements.txt:

pip install -r requirements.txt

#Zastosuj migracje do bazy danych:

python manage.py migrate

#Uruchom serwer deweloperski:

python manage.py runserver

#Otwórz przeglądarkę internetową i przejdź pod adres:

http://localhost:8000
