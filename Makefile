
bench:
	/bin/bash test/bench.sh http://172.17.0.2:8888

all: test

test:
	pytest --cov=./ test

test-ui:
	pytest --cov=./ --cov-report=html test

generate: generate-server generate-client

generate-server:
	js9_raml generate_pyserver

generate-client:
	js9_raml generate_pyclient

.PHONY: test test-ui generate generate-server generate-client
