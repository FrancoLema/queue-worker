.PHONY: format-code

format-code:
	poetry run black .

lint:
	poetry run mypy .