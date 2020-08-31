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
Program `genlog.py` can generate a fixed-width file with the specified encoding.
- -h Will show the usage of the program.
- -c Name of configuration file.
- -o Name of output file.
- -l Number of lines in the output file. 


## Parse Fixed Width File
~~~bash
docker run -it --rm -v $PWD:/usr/src/app -w /usr/src/app mypython3:sz82 \
  python3 parser.py -c spec.json -i text.log -o text.csv

~~~
Program `parser.py` can parse the fixed-width file and generate a delimited file with the specified encoding.
- -h Will show the usage of the program.
- -c Name of configuration file.
- -i Name of input file.
- -o Name of output file.


## Check Parsing Result File
~~~bash
docker run -it --rm -v $PWD:/usr/src/app -w /usr/src/app mypython3:sz82 \
  python3 check2f.py -c spec.json -i text.log,text.csv

~~~
Program `check2f.py` can compare the content of the fixed-width file and the delimited file with the specified encoding.
- -h Will show the usage of the program.
- -c Name of configuration file.
- -i Name of input files, separated by comma like 'file1,file2'.


