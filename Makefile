all: download_deps collectstatic

collectstatic:
	python manage.py collectstatic

download_deps:
	rm -rf vendor/*
	pip install -t vendor -r requirements.txt
