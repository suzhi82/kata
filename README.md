# The answer to Coding Challenges

## Get Source Files
~~~bash
git clone https://github.com/suzhi82/kata.git
cd kata/src && ls -1
# Dockerfile
# check2f.py
# demo.sh
# genlog.py
# parser.py
# spec.json
~~~


## Demo Shell Script
You can simply use the command below to make life easier.​ :smirk:
~~~bash
bash demo.sh
~~~
Alternative you can also follow the order below step by step.


## Build Docker Image
~~~bash
docker build -t mypython3:sz82 .
~~~


## Generate Fixed Width File
~~~bash
docker run -it --rm -v $PWD:/usr/src/app -w /usr/src/app mypython3:sz82 \
  python3 genlog.py -c spec.json -o text.log -l 300

~~~


## Parse Fixed Width File
~~~bash
docker run -it --rm -v $PWD:/usr/src/app -w /usr/src/app mypython3:sz82 \
  python3 parser.py -c spec.json -i text.log -o text.csv

~~~


## Check Parsing Result File
~~~bash
docker run -it --rm -v $PWD:/usr/src/app -w /usr/src/app mypython3:sz82 \
  python3 check2f.py -c spec.json -i text.log,text.csv

~~~


