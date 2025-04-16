install:
	pip install -r requirements.txt

test:
	pytest tests/

run:
	uvicorn src.api.app:app --reload
