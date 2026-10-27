# Cykl pracy Dockerfile -(docker bulid)-> Obraz Dockera -(docker run)-> Kontener
FROM python:3.12

WORKDIR /app

# Kopiuje plik z kontekstu budowania do katalogu roboczego
# Pierwsza kropka oznacza źródło, druga kropka oznacza miejsce docelowe
# COPY nie wybiera automatycznie potrzebnych plików, stąd stosowanie .dockerignore
COPY . .

# Podczas budowania obrazu instaluje naszą plikację i jej zależności. Kropka na końcu oznacza bieżący katalog, w którym znajduje się pyproject.toml
# --no-cache-dir - nie zapisuje pamięci podręcznej pobranych pakietów pip
RUN pip install --no-cache-dir .

# określenie polecenia uruchomieniowego
CMD ["research-analyzer"]