.PHONY: all pytest newman clean

all: pytest newman

pytest:
	python scripts/run_pytests.py

newman:
	python scripts/run_newman.py

clean:
	rm -rf __pycache__ .pytest_cache reports/*
