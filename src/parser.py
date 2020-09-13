#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json


def intercept(line, pos):
    res, i = [], 0
    for j in pos:
        res.append(line[i:(j + i)])
        i += j
    return res


def parser(conf_file, input_file, output_file):
    with open(conf_file, mode='r', encoding='utf-8') as cf:
        conf = json.load(cf)
        input_encoding = conf['FixedWidthEncoding']
        output_encoding = conf['DelimitedEncoding']
        include_header = conf['IncludeHeader']
        headers = conf['ColumnNames']
        offsets = list(map(int, conf['Offsets']))

    with open(input_file, mode='r', encoding=input_encoding) as in_put, \
            open(output_file, mode='w', encoding=output_encoding) as out_put:
        if include_header.upper() == "TRUE":
            out_put.write(",".join(headers) + '\n')
        line = in_put.readline()
        while line:
            str_arr = intercept(line, offsets)
            out_put.write(",".join(str_arr) + '\n')
            line = in_put.readline()


if __name__ == "__main__":
    parser(sys.argv[1], sys.argv[2], sys.argv[3])
