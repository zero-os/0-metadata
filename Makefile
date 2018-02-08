all: test

test:
	pytest --cov=./ tests

test-ui:
	pytest --cov=./ --cov-report=html tests

generate: generate-server

generate-server:
	js9_raml generate_pyserver
generate-client:
	js9_raml generate_pyclient


.PHONY: all test test-ui generate generate-server generate-client