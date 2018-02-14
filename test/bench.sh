#! /bin/bash

usage() {
    echo "Usage: $0 [URL] [rate]"
    echo "  URL: Url to benchmark (default: http://127.0.0.1:5000)"
    echo " rate: request per second (default: 50)"
}

clean() {
    rm -Rf ${targets}
    popd >/dev/null
    echo "CLEANING"
    exit 0
}

a=$(which vegeta) 
[ $? -ne 0 ] && echo "Vegeta Dependency missing" && exit 1

[ "$1" == "" -o "$2" == "" ] &&   usage

url="${1:-http://127.0.0.1:5000}"
rate="${2:-50}"
secs="30s"
rdir=$(dirname $0)
targets="./targets"
maxrecords=999

pushd ./
cd ${rdir}
trap clean ERR

mkdir -p ${targets}
echo -n "" > "${targets}/POST"
echo -n "" > "${targets}/GET"
echo -n "" > "${targets}/LIST"
echo -n "" > "${targets}/DEL"
for i in $(seq 1 ${maxrecords}); do 
    body="{\"uid\": $i,\"addr\": \"home\", \"alias\": [\"jsmith\"], \"keyPub\": [\"123\"]}"
    echo $body > "./targets/jsbody.${i}"
    echo "POST ${url}/user/${i}" >> "${targets}/POST"
    echo "Content-Type: application/json" >> "${targets}/POST"
    echo "@./targets/jsbody.${i}" >> "${targets}/POST"
    echo >> "${targets}/POST"
    echo "GET ${url}/user/${i}" >> "${targets}/GET"
    echo "GET ${url}/user" >> "${targets}/LIST"
    echo "DELETE ${url}/user/${i}" >> "${targets}/DEL"
done 

for i in POST GET LIST DEL; do
    echo -n "${i}..."
    vegeta attack -targets=${targets}/${i} -duration=${secs} -rate=${rate} > result.${i}
    cat result.POST | vegeta report -reporter=plot > plot.${i}.html
done

echo -e "\r***** Summary Report *****    \r"
for i in POST GET LIST DEL; do
    echo -e "\n${i}"
    cat result.${i} | vegeta report
done

clean
