all: clean download_requirements 

clean:
	rm -rf vendor/*

download_requirements:
	pip install -t vendor --install-option=--prefix='' --no-deps -r requirements.txt
