#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import getopt
import json
import sys


def main(argv):
    confs_file = ''
    input_file = ''
    output_file = ''
    delimiter = ','
    endofline = '\n'
    utf8alias = ['utf-8', 'U8', 'UTF', 'utf8', 'cp65001']
    usage = argv[0] + ' -c <confsfile> -i <inputfile> -o <outputfile>'

    try:
        opts, args = getopt.getopt(argv[1:], "hc:i:o:")
    except getopt.GetoptError as err:
        print(err)
        print(usage)
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit(0)
        elif opt == '-c':
            confs_file = arg
        elif opt == '-i':
            input_file = arg
        elif opt == '-o':
            output_file = arg

    if confs_file == '' or input_file == '' or output_file == '':
        print('Essential parameters required')
        print(usage)
        sys.exit(1)

    try:
        confs_fp = open(confs_file, mode='r')
        confs = json.load(confs_fp)

        in_encoding = confs['FixedWidthEncoding']
        input_fp = open(input_file, mode='r', encoding=in_encoding)

        out_encoding = confs['DelimitedEncoding']
        # UTF8 with BOM for opening correctly by MS Excel
        if out_encoding in utf8alias:
            out_encoding = 'utf-8-sig'
        output_fp = open(output_file, mode='w', encoding=out_encoding)

        if confs['IncludeHeader'].upper() == 'TRUE':
            fields = ','.join(confs['ColumnNames']) + endofline
            output_fp.write(fields)

        offsets = list(map(int, confs['Offsets']))
        offsum = sum(offsets)
        line = input_fp.readline()
        while line.strip():
            i = 0
            oline = ''
            for j in offsets:
                j += i
                if j == offsum:
                    oline += line[i:j] + endofline
                else:
                    oline += line[i:j] + delimiter
                i = j
            output_fp.write(oline)

            line = input_fp.readline()

    except IOError as err:
        print(err)

    except ValueError as err:
        print(err)

    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

    finally:
        if 'confs_fp' in dir():
            confs_fp.close()

        if 'input_fp' in dir():
            input_fp.close()

        if 'output_fp' in dir():
            output_fp.flush()
            output_fp.close()


if __name__ == '__main__':
    main(sys.argv)
