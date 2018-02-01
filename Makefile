

generate: generate-server

generate-server:
	go-raml server -l go --dir api --ramlfile specs/main.raml --no-apidocs
	raml2html -p specs/main.raml > specs/api.html