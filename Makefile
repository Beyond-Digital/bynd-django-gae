all: clean download_deps

download_deps:
	mkdir build
	pip install -t build -r requirements.txt
	rm -f lib/vendor.zip
	cd build && zip -r ../lib/vendor.zip *

clean:
	rm -rf build
	rm -rf lib/vendor.zip