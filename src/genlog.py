#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import getopt
import json
import os
import sys


def main(argv):
    confs_file = 'spec.json'
    output_file = 'test.log'
    line_count = 100
    schar = 'á'
    endofline = '\n'
    usage = argv[0] + ' -c <confsfile> -o <outputfile> -l <linecount>'

    try:
        opts, args = getopt.getopt(argv[1:], "hc:o:l:")
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
        elif opt == '-o':
            output_file = arg
        elif opt == '-l':
            line_count = int(arg)

    try:
        confs_fp = open(confs_file, mode='r')
        confs = json.load(confs_fp)

        fields = list(map(lambda x: '%' + x + 's', confs['Offsets']))
        print(fields)

        line_str = ''
        for f in fields:
            line_str += f % schar
        line_str += endofline

        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.mkdir(output_dir)
        output_fp = open(output_file, mode='w', encoding=confs['FixedWidthEncoding'])

        print(output_fp.encoding)
        for i in range(line_count):
            # print(line_str, end='')
            output_fp.write(line_str)

    except IOError as err:
        print(err)

    except:
        print("Unexpected error:", sys.exc_info()[0])

    finally:
        if 'confs_fp' in dir():
            confs_fp.close()

        if 'output_fp' in dir():
            output_fp.flush()
            output_fp.close()


if __name__ == '__main__':
    main(sys.argv)
