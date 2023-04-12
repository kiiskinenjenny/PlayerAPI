# Vaadittavat asennukset Windows

## Virtuaaliympäristö

### Luo virtuaaliympäristö:

View - Command Palette - Python: Create Environment... - Venv

### Aktivoi Venv:

Varmistathan, että olet PlayerAPI-kansion juuressa.
New Terminal: .venv/Scripts/Activate.ps1

Terminaalissa pitäisi näkyä vihreällä värillä (.venv)

## Kirjastot

### Ajaa seuraavia komentoja terminaalissa:

pip install fastapi uvicorn
pip install sqlalchemy fastapi uvicorn

# Ohjelman käynnistäminen

Ajaa terminaalissa:
uvicorn app.main:app --reload
