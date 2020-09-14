#!/usr/bin/env bash


_dimg="mypython3:v3.6"
_wkdir="/usr/src/app"
_dcmd="docker run -it --rm -v $PWD:$_wkdir -w $_wkdir $_dimg python3"


echo -e "\n========== 0. Building Docker Image ================"
[ ! -z $(docker images -q $_dimg) ] || docker build -t $_dimg .


echo -e "\n========== 1. Generating Fixed Width File =========="
_cmd="$_dcmd genfixed.py"
echo $_cmd
time $_cmd


echo -e "\n========== 2. Parsing Fixed Width File ============="
_cmd="$_dcmd parser.py spec.json fixed.txt delim.csv"
echo $_cmd
time $_cmd


echo -e "\n========== 3. Running Unit Test Cases =============="
_cmd="$_dcmd -m unittest test_parser"
echo $_cmd
time $_cmd



