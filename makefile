all:
	python scripts/run_all_test.py

pytest:
	python scripts/run_pytests.py

newman:
	python scripts/run_newman.py

clean:
	rm -rf reports/
	rm -rf gh-pages/
