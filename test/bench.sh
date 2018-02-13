#! /bin/bash

usage() {
    echo "Usage: $0 [URL]"
    echo "  URL: Url to benchmark ie: http://172.16.0.2:8888"
    exit 1
}


a=$(which vegeta) 
[ $? -ne 0 ] && echo "Vegeta Dependency missing" && exit 1

[ "$1" = "" ] && usage

url="$1"

secs="10s"
targets="./targets"
maxrecords=999


echo -n "POST..."
mkdir -p ${targets}
postfile="${targets}/POST"
getfile="${targets}/GET"
delfile="${targets}/DEL"
echo -n "" > ${postfile}
echo -n "" > ${getfile}
echo -n "" > ${delfile}
for i in $(seq 1 ${maxrecords}); do 
    body="{\"uid\": $i,\"addr\": \"home\", \"alias\": [\"jsmith\"], \"keyPub\": [\"123\"]}"
    echo $body > "./targets/jsbody.${i}"
    echo "POST ${url}/user/${i}" >> ${postfile}
    echo "Content-Type: application/json" >> ${postfile}
    echo "@./targets/jsbody.${i}" >> ${postfile}
    echo >> ${postfile}
    echo "GET ${url}/user/${i}" >> ${getfile}
    echo "DELETE ${url}/user/${i}" >> ${delfile}
done 

vegeta attack -targets=${postfile} -duration=${secs} > result.POST
cat result.POST | vegeta report -reporter=plot > plot.POST.html

echo -n "GET..."
vegeta attack -targets=${getfile} -duration=${secs} > result.GET
cat result.GET |vegeta report -reporter=plot > plot.GET.html

echo -n "LIST..."
echo "GET ${url}/user" | \
vegeta attack  -duration=${secs} > result.LIST
cat result.LIST | vegeta report -reporter=plot > plot.LIST.html

echo -n "DELETE..."
vegeta attack -targets=${delfile} -duration=${secs} > result.DEL
cat result.DEL | vegeta report -reporter=plot > plot.DEL.html


echo -e "\r***** Summary Report *****    \r"
for i in POST GET LIST DEL; do
    echo -e "\n${i}"
    cat result.${i} | vegeta report
done

rm -Rf ${targets}
