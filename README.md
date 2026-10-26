# RESEARCH DATA ANALYZER

Aplikacja konsolowa napisana w języku Python, przeznaczona do wczytywania, analizy i zapisywania danych pogodowych.

Projekt powstał w ramach szkolenia **"Projektowanie i programowanie aplikacji w Pythonie..."**


## Spis treści
1. [Funkcjonalności](#1-funkcjonalności)
2. [Wykorzystane technologie](#2-wykorzystne-technologie)
3. [Struktura projektu](#3-struktura-projektu)
4. [Instalacja](#4-instalacja)
5. [Uruchamianie aplikacji](#5-uruchamianie-aplikacji)
6. [Analiza danych](#6-analiza-danych)
7. [Testowanie](#7-testowanie)
8. [Kontrola jakości kodu](#8-kontrola-jakosci-kodu)
9. [Automatyzacja CI](#9-automatyzacja-ci)
10. [Zastosowanie](#10-zastosowanie)

## 1. Funkcjonalności

Aplikacja umożliwia:
- wczytywanie danych pogodowych z pliku CSV
- wyświetlanie podglądu danych z wykorzystaniem biblioteki Pandas
- obliczanie podstawowych statystyk
- generowanie i zapisywanie wykresów
- zapisywanie danych do bazy SQLite
- obsługę programu przez interaktywne menu konsolowe

## 2. Wykorzystane technologie

- **Python** - język programowania
- **Pandas** - przetwarzanie i analiza danych
- **Matplotlib** - wizualizacja danych
- **SQLite** - przechowywanie danych w relacyjnej bazie danych
- **Termcolor** - kolorowanie komunikatów w konsoli
- **Pytest** - testy jednostkowe
- **Ruff** - kontrola jakości kodu
- **Git i GitHub** - kontrola wersji i przechowywanie repozytorium
- **GitHub Actions** - automatyczne uruchamianie testów i kontrola jakości kodu

## 4. Instalacja

Do uruchomienia aplikacji potrzebny jest Python w wersji 3.12+ oraz biblioteki wymienione w pliku `requirements.txt`.

Po pobraniu projektu należy przejść do jego katalogu i utworzyć środowisko wirtualne:
```bash
python -m venv .venv
```

Aktywacja środowiska w systemie Windows (PowewrShell):
```bash
.\.venv\Scripts\Activate.ps1
```

Instalacja zależności:
```bash
python -m pip install -r requirements.txt
```

## 5. Uruchamianie

W katalogu głównym projektu wykonujemy:
```bash
python main.py
```

Po uruchomieniu pojawia się menu:
```text
RESEARCH DATA ANALYZER
1. Wczytaj dane z pliku csv
2. Wyświetl dane
3. Analizuj dane
4. Generuj i zapisz wykres
5. Zapisz dane do bazy
0. Wyjście z programu
```

Aby rozpocząć pracę należy umieścić pliki CSV w katalogu `\data`

## 8. Kontrola jakości kodu

Do analizy kodu wykorzystujemy **Ruff**

Sprawdzenie kodu:
```bash
python -m ruff check .
```

Automatyczne poprawianie obsługiwanych problemów:
```bash
python -m ruff check . --fix
```

## 10. Zastosowanie

Aplikacja może stanowić punkt wyjścia do przetwarzania danych wykorzystywanych w pracy naukowej lub dydaktycznej.

Przykładowe zastosowania obejmują analizę danych pomiarowych, przygotowanie prostych zestawień statystycznych, wizualizację wyników oraz archiwizowanie danych w bazie danych.

Projekt ma **charakter edukacyjny** i może być rozwijany o kolejne funkcjonalności.
