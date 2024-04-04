1.Sklonuj repozytorium na swój lokalny komputer:

$git clone <URL_repozytorium>

2.Utwórz wirtualne środowisko Pythona:

$python3 -m venv venv

3.Aktywuj wirtualne środowisko:
$source venv/bin/activate

4.Zainstaluj wymagane pakiety Pythona z pliku requirements.txt:

$pip install -r requirements.txt

5.Zastosuj migracje do bazy danych:

$python manage.py migrate

6.Uruchom serwer deweloperski:

$python manage.py runserver

7.Otwórz przeglądarkę internetową i przejdź pod adres:

$http://localhost:8000
