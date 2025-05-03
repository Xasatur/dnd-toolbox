# DnD Toolbox

Welcome to the **DnD Toolbox** – a modular command-line application for Dungeons & Dragons game masters. This tool helps you manage spells, generate loot, and simulate monster combat behavior.

---

# Setup Instructions

Run the following commands to set up the project:

```bash
pyenv install 3.10.6
pyenv virtualenv 3.10.6 dnd_env
pyenv activate dnd_env
pip install -r requirements.txt
```
The application expects a `.env` file for environment configuration.

Optionally, create a .python-version file with the content dnd_env to auto-activate the environment when entering the project folder.


---

# How to Run

Use the following to launch the toolbox:

```bash
cd src/core
python Toolbox.py
```

The toolbox will present a menu to access the Spellbook, Looter, and Combat modules.

---

# How to Launch the Interface


To start both the backend (FastAPI) and the frontend (Streamlit), run:

```bash
make run


---

# Example Commands

```bash
python Toolbox.py
```

More CLI arguments will be added.

---

# CLI

Basic CLI interaction is available through user menu selections inside `Toolbox.py`.

---

# API

Implemented using FastAPI. Available endpoints:

	•	GET /loot?rarity=rare – Filter loot by rarity
	•	GET /spells?level=3 – Filter spells by level
	•	GET /monsters – List available monsters
	•	POST /combat – Submit a combat round (coming soon)

The backend is served with uvicorn.

---

# Frontend (Streamlit UI)

A simple web interface allows users to:
	•	Search spells by name, class, level, school
	•	Generate loot by rarity
	•	Simulate combat by selecting monsters and triggering their actions

Streamlit is used to render the UI at localhost:8501.

---

# Docker

A Dockerfile is provided to containerize the entire project. Build and run with:

```bash
docker build -t dnd_toolbox .
docker run -p 8000:8000 -p 8501:8501 dnd_toolbox
```

Make sure ports 8000 and 8501 are available.

This launches both API and Streamlit UI in a container.



---

# Packaging (setup.py)

This project uses Python packaging conventions:
	•	setup.py defines the installable structure
	•	Install it locally with:

```bash
pip install .
```

---

# Testing & Automation

The project includes automated tests using `pytest`.

### Run all tests

```bash
make test
```

### Format code with Black

```bash
make format
```

### Check code quality with Flake8

```bash
make lint
```

### Run all steps at once (test, format, lint)

```bash
./autotest.sh
```


# Expected Output

- Spells filtered by name, school, class, level
- Loot items based on rarity
- Monster actions simulated through a text interface

---

# Dependencies and Environment Info

Main libraries used:

- `dotenv`
- `pytest`
- `FastAPI` (planned)
- `Streamlit` (planned)

Python version: **3.10.6**

Virtual environment created using `pyenv` and `pyenv-virtualenv`.

---

# Credits

- Created by Leonardo Cesconi
- Project for the IAI Module @ HSLU (Spring 2025)
- JSON content partially based on SRD / DnD 5e Open Content

---
