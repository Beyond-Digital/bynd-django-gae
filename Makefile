all: download_requirements collectstatic

clean:
	rm -rf vendor/*

collectstatic:
	./manage.py collectstatic --noinput

download_requirements:
	cmp -s requirements.txt vendor/requirements.txt; \
  	RETVAL=$$?; \
  	if [ $$RETVAL -eq 0 ]; then \
		echo "Dependencies up-to-date"; \
  	else \
		echo "Dependencies need updating"; \
		make clean; \
    		pip install -t vendor --install-option=--prefix='' --no-deps -r requirements.txt && cp requirements.txt vendor/; \
  	fi

