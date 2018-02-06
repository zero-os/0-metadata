
generate: generate-server generate-client

generate-server:
	js9_raml generate_pyserver

generate-client:
	js9_raml generate_pyclient