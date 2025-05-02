from setuptools import setup, find_packages

setup(
    name="dnd_toolbox",
    version="0.1.0",
    author="Leonardo Cesconi",
    description="A modular DnD assistant with combat, loot, spellbook and API/frontend features.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "fastapi",
        "uvicorn",
        "streamlit",
        "python-dotenv",
        "black",
        "flake8",
        "pytest",
    ],
    python_requires=">=3.10",
)
