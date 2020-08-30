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
    sflag = True

    # Get parameters
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

    # Check parameters
    if confs_file == '' or input_file == '' or output_file == '':
        print('Essential parameters required')
        print(usage)
        sys.exit(1)

    # Prompt files' name
    print(
        "confs_file = {0}\ninput_file = {1}\noutput_file = {2}"
        .format(confs_file, input_file, output_file)
    )

    try:
        # Load configuration
        confs_fp = open(confs_file, mode='r')
        confs = json.load(confs_fp)

        # Open the source file with the specified encoding
        in_encoding = confs['FixedWidthEncoding']
        input_fp = open(input_file, mode='r', encoding=in_encoding)

        # Open the target file with the specified encoding
        out_encoding = confs['DelimitedEncoding']
        # Use UTF8-BOM to build the target file for opening correctly by MS Excel
        if out_encoding in utf8alias:
            out_encoding = 'utf-8-sig'
        output_fp = open(output_file, mode='w', encoding=out_encoding)

        # Prompt input output encoding
        print("{0} ==> {1}".format(input_fp.encoding, output_fp.encoding))

        # Determine whether to add column headers
        include_header = confs['IncludeHeader']
        if include_header.upper() == 'TRUE':
            fields = delimiter.join(confs['ColumnNames']) + endofline
            output_fp.write(fields)

        # Get the width of each field
        offsets = list(map(int, confs['Offsets']))
        line_width = sum(offsets)
        # Read the source file in a loop
        line = input_fp.readline()
        while line.strip():
            i = 0
            oline = ''
            for j in offsets:
                j += i
                # Determine whether to reach the end of the line
                if j == line_width:
                    oline += line[i:j] + endofline
                else:
                    oline += line[i:j] + delimiter
                i = j
            # Put a line to target file
            output_fp.write(oline)
            # Read a line from source file
            line = input_fp.readline()

    except IOError as err:
        sflag = False
        print(err)
        raise err

    except ValueError as err:
        sflag = False
        print(err)
        raise err

    except:
        sflag = False
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

        if sflag:
            print("Succeeded")
        else:
            print("Failed")


if __name__ == '__main__':
    main(sys.argv)
