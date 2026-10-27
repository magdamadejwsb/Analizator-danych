# Uruchamianie aplikacji
import logging

from interfejs import uruchum_menu
from logowanie import konfiguruj_logowanie


def main():
    """Uruchamia menu glowne aplikacji"""

    konfiguruj_logowanie()
    logging.info("Uruchomiono aplikacje")

    uruchum_menu()

    logging.info("Zakończono działanie aplikacji")

# warunek uruchamiania programu - określa czy dany plik został uruchomiany bezpośrednio, czy został zaimportowany jako moduł z innego pliku
# __name__ - zmiena automatycznie ustawiana przez Pythona dla każdego modułu
# "__main__" - wartość oznaczająca moduł uruchamiany jako główny program

if __name__ == "__main__":
    main()    