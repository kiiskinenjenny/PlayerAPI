# Vaadittavat asennukset Windows

## Virtuaaliympäristö

### Luo Venv:

View - Command Palette - Python: Create Environment... - Venv
<br />

### Aktivoi Venv:

Varmistathan, että olet PlayerAPI-kansion juuressa. <br />
New Terminal: .venv/Scripts/Activate.ps1 <br />

Terminaalissa pitäisi näkyä (.venv) vihreällä värillä.
<br />

## Kirjastot

### Ajaa seuraavia komentoja terminaalissa:

pip install fastapi uvicorn <br />
pip install sqlalchemy fastapi uvicorn <br />
<br />

# Ohjelman käynnistäminen

Ajaa terminaalissa: <br />
uvicorn app.main:app --reload
