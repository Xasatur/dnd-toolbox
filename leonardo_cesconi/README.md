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

An interactive user interface is planned with Streamlit. Current interaction is through the command line.

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

An API will be implemented using FastAPI.


- `GET /loot?rarity=rare`
- `GET /spells?level=3`

---

# Docker

A Dockerfile will be added.

```bash
docker build -t dnd_toolbox .
docker run -p 8000:8000 dnd_toolbox
```

---

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
