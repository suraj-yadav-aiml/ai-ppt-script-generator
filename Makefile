.PHONY: run install
.DEFAULT_GOAL:=run

run: install
	poetry run streamlit run streamlit_app/app.py

install:
	poetry install

clean:
	rm -rf `find . -type d -name __pycache__`