# Installiere alle Abhängigkeiten aus requirements.txt
install:
	pip install -r requirements.txt

# Führe alle Tests im tests/ aus

test:
	PYTHONPATH=. pytest tests

format:
	black .

lint:
	flake8 .

# Starte FastAPI-Server
run:
	uvicorn src.api.app:app --reload
