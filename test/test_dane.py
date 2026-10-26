import pandas as pd

from dane import wyswietl_dane, wczytaj_dane


def test_wyswietl_dane(capsys):
    df = pd.DataFrame({
        "miasto": ["Szczecin", "Warszawa"],
        "temp_max": [22, 24]
    })

    wyswietl_dane(df)

    wynik = capsys.readouterr().out

    assert "Liczba rekordów: 2" in wynik
    assert "Liczba kolumn: 2" in wynik
    assert "Koluny: miasto, temp_max" in wynik


def test_wyswietl_dane_brak(capsys):
    wyswietl_dane(None)

    wynik = capsys.readouterr().out

    assert "Najpierw wczytaj plik CSV" in wynik

# Testowanie funkcji wczytaj_dane
# tmp_path - tymczasowy katalog na potrzeby testu
# monkeypatch - pozwala tymczasowo zmienic katalog roboczy i zasymulować odpowiedz użytkownika

def test_wczytaj_dane(tmp_path, monkeypatch):
    folder = tmp_path / "data"
    folder.mkdir()

    plik = folder / "pogoda.csv"
    plik.write_text(
        "miasto, temp_max\n"
        "Szczecin,22\n"
        "Warszawa,24\n",
        encoding="utf-8"
    ) 

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr("builtins.input", lambda _: "1")
    # monkeypatch.setattr() - metoda pytest, która pozwala tymczasowo podmienić funkcję lub atrybut
    # builtins - moduł, który zawiera funkcje wbudowane Pythona
    # input - funkcja, która pobiera dane od użytkownika
    # lambda _: "1" - wskazujemy, że chcemy zasymulować wybór 1

    df = wczytaj_dane()

    assert df is not None
    assert f"Liczba wierszy: {len(df)}"


def test_wczytaj_dane_brak_plikow(tmp_path, monkeypatch, capsys):
    folder = tmp_path / "data"
    folder.mkdir() 

    monkeypatch.chdir(tmp_path)

    wynik = wczytaj_dane()
    komunikat = capsys.readouterr().out

    assert wynik is None
    assert "Brak plików" in komunikat



