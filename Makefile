.PHONY: test run

test:
	poetry run pytest

run:
	poetry run uvicorn auth_app.app:app --reload
