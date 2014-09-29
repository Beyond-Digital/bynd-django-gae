all: clean download_requirements collectstatic

clean:
	rm -rf vendor/*

collectstatic:
	./manage.py collectstatic --noinput

download_requirements:
	pip install -t vendor --install-option=--prefix='' --no-deps -r requirements.txt
