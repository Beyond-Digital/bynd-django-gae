all: download_deps

download_deps:
	rm -rf vendor/*
	pip install -t vendor -r requirements.txt
