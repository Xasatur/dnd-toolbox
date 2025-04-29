# 🚀 Project Submission Guidelines

Welcome to the **hands-on project** component of this course! This README outlines everything you need to know to **successfully complete, document, and submit** your project.

---

## 🗂️ Where and How to Submit

All submissions must be pushed to **GitLab** in the following structure:

- Navigate to the folder:  
  `Project_Submissions_Students/`

- Name your submission folder using your **full name** in lowercase, joined with underscores:

  ```
  name_surname/
  ```

- If working in a group of **2 students** (maximum allowed!), name your folder as:

  ```
  name1_surname1_name2_surname2/
  ```

❗ *Note: Group work is allowed (max 2 students), but individual submissions are strongly preferred.*

---

## 📌 Project Requirements & Evaluation Criteria

### 1. Project Structure

Your submission should follow the **recommended folder structure** as we discussed during the lectures and I have shown you in the examples.  

Include sub-folders that make sense for your project, e.g.:

```
📁 data/
📁 src/
📁 tests/
📁 notebooks/
📁 docs/
```

---

### 2. pyenv-virtualenv

Set up and manage isolated Python environments for your project using:

```bash
pyenv install 3.10.6
pyenv virtualenv 3.10.6 myenv
pyenv activate myenv
```

Ensure your virtual environment is **activated in your shell** and that dependencies are installed into it via `pip`.


### 3. Python Modules & Packaging

Organize your code into reusable modules and packages. Your folder structure should reflect modularity, e.g.:

```
📁 src/
   ┣ 📄 __init__.py
   ┣ 📄 data_loader.py
   ┗ 📄 model.py
```

Each file should encapsulate a specific functionality and use `import` statements correctly.

Please make the package out of your code as we have seen in the Lecture (use `setup.py` for example). 


### 4. Command-Line Arguments

Your scripts should accept arguments from the terminal.

📌 Example : Greeting a user

```python
# hello.py
import sys

print("Script name:", sys.argv[0])
print("Hello,", sys.argv[1])
```

`sys.argv` stores all arguments passed from the command line as strings in a list. `sys.argv[0]` is always the script name.

💡 For better user interaction, use `argparse`. 

Use Python’s built-in `argparse` module to allow your scripts to accept command-line arguments like here:

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str, help="Input file path")
args = parser.parse_args()
```

Document expected arguments in your README.


### 5. Environment Variables

Configure settings using `.env` files and access them with Python:

```bash
# .env
API_KEY=abc123
```

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
```

Ensure `.env` is excluded from Git tracking using `.gitignore`.


### 6. Makefiles and Testing

Automate your workflow using `Makefile`. Include targets such as:

```makefile
install:
	pip install -r requirements.txt

test:
	pytest tests/
```

You may use either `pytest` or Python's `unittest` framework for writing tests. Make sure tests are included in the `tests/` directory.


### 7. Shell Automation: `autotest.sh` Script

Include a shell script called:

```bash
autotest.sh
```

This script should reproduce the functionality of the `Makefile` we discussed — automating:
- testing
- formatting
- linting
- any other CI-relevant steps

---

### 8. API Integration

Use a **Python-based API framework** (such as [FastAPI](https://fastapi.tiangolo.com/)) to build a minimal REST API for your project functionality.

You should:
- Document all routes
- Include input/output examples
- Test at least one endpoint

---

### 9. Docker

Use **Docker** to containerize your project:

- Include a `Dockerfile` with appropriate configuration
- Add `docker-compose.yml` if needed
- Document how to build and run the image:
  
```bash
docker build -t myproject .
docker run -p 8000:8000 myproject
```

---

### 10. Interactive Frontend

Integrate your backend with an interface using one of the following:

- [Streamlit](https://streamlit.io/)
- [Chainlit](https://www.chainlit.io/)

Make sure:
- The interface works smoothly
- All components are interactive and demonstrate your model/project logic
- Include instructions in the README for how to launch the interface

---

## Git & GitLab/GitHub Usage

Push your project regularly and **track progress** using Git. We expect to see:

- Proper commits with clear messages
- Use of branches (optional but appreciated)
- Collaboration (for teams) through merge requests

> 💡 *GitLab is not optional — it's your main submission portal.*

---

## 📘 Required: Project README File

Each student (or group) must include a `README.md` file **within their project folder**.

This file should contain:

- ✅ **Project title and description**
- ✅ **Setup instructions**
- ✅ **How to run the project**
- ✅ **Example commands** with explanations (e.g., CLI arguments, Docker commands, API calls)
- ✅ **Expected outputs**
- ✅ **Dependencies and environment info**
- ✅ **Credits** (if working in a group or using external resources)

> 💡 Your README will be a key part of the peer review and presentation, so keep it clean, clear, and complete!

---

## 👥 Peer Review & Grading

✅ **Grading will be based on peer review**. 

The Lecturer will monitor for fairness and step in if needed.

---

## 🎤 Final Presentations: **May 12th**

Each student will present their project, including:
- Architecture
- Code walkthrough
- Live demo

⏱ **Time limits:**
- Individual: **10 minutes**
- Group of 2: **15 minutes total**

Practice beforehand! 💻

---