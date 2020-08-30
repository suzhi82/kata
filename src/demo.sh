#!/usr/bin/env bash


_dimg="mypython3:sz82"
_wkdir="/usr/src/app"
_dcmd="docker run -it --rm -v $PWD:$_wkdir -w $_wkdir $_dimg python3"


# 0. Build Docker Image
[ ! -z $(docker images -q $_dimg) ] || docker build -t $_dimg .


echo -e "\n========== 1. Generate Log File =========="
_cmd="$_dcmd genlog.py -c spec.json -o text.log -l 300"
echo $_cmd
time $_cmd


echo -e "\n========== 2. Parse Log File ============="
_cmd="$_dcmd parser.py -c spec.json -i text.log -o text.csv"
echo $_cmd
time $_cmd


echo -e "\n========== 3. Check Files Content ========"
_cmd="$_dcmd check2f.py -c spec.json -i text.log,text.csv"
echo $_cmd
time $_cmd



