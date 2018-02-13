#! /bin/bash

usage() {
    echo "Usage: $0 [URL]"
    echo "  URL: Url to benchmark ie: http://172.16.0.2:8888"
    exit 1
}


which vegeta
[ $? -ne 0 ] && echo "Vegeta Dependency missing" && exit 1

[ "$1" = "" ] && usage

url="$1"

secs="50s"

mkdir ./targets
file="./targets/POST"
echo -n "" > ${file}
for i in $(seq 1 1000); do 
    body="{\"uid\": $i,\"addr\": \"home\", \"alias\": [\"jsmith\"], \"keyPub\": [\"123\"]}"
    echo $body > "./targets/jsbody.${i}"
    echo "POST ${url}/user/${i}" >> ${file}
    echo "Content-Type: application/json" >> ${file}
    echo "@./targets/jsbody.${i}" >> ${file}
    echo >> ${file}
done 

vegeta attack -targets=${file} -duration=$secs | \
vegeta report -reporter=plot > plot.POST.html

echo "GET"
file="./targets/GET"
echo -n "" > ${file}
for i in $(seq 1 1000); do 
    echo "GET ${url}/user/${i}" >> ${file}
done

vegeta attack -targets=${file} -duration=$secs| \
vegeta report -reporter=plot > plot.GET.html

echo "LIST"
echo "GET ${url}/user" | \
vegeta attack  -duration=$secs | \
vegeta report -reporter=plot > plot.LIST.html

echo "DELETE"
file="./targets/DELETE"
echo -n "" > ${file}
for i in $(seq 1 1000); do 
    echo "DELETE ${url}/user/${i}" 
done

vegeta attack -targets=${file} -duration=10s | \
vegeta report -reporter=plot > plot.DEL.html
