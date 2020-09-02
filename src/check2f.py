#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import getopt
import json
import sys


def main(argv):
    confs_file = ''
    input_file1 = ''
    input_file2 = ''
    line_count = 0
    line_error = []
    usage = argv[0] + ' -c <confsfile> -i <inputfile1,inputfile2>'

    # Get parameters
    try:
        opts, args = getopt.getopt(argv[1:], "hc:i:")
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
            input_file1, input_file2 = str.split(arg, ",")

    # Check parameters
    if confs_file == '' or input_file1 == '' or input_file2 == '':
        print('Essential parameters required')
        print(usage)
        sys.exit(1)

    # Prompt
    print(
        "confs_file = {0}\ninput_file1 = {1}\ninput_file2 = {2}"
        .format(confs_file, input_file1, input_file2)
    )

    try:
        # Load configuration
        confs_fp = open(confs_file, mode='r')
        confs = json.load(confs_fp)

        # Open the input file1 with the specified encoding
        in_encoding1 = confs['FixedWidthEncoding']
        input_fp1 = open(input_file1, mode='r', encoding=in_encoding1)

        # Open the input file2 with the specified encoding
        in_encoding2 = confs['DelimitedEncoding']
        input_fp2 = open(input_file2, mode='r', encoding=in_encoding2)

        offsets = list(map(int, confs['Offsets']))
        line1 = input_fp1.readline()
        if confs['IncludeHeader'].upper() == 'TRUE':
            input_fp2.readline()

        # Compare the contents of inputfile1 and inputfile2
        while line1.strip():
            line_count += 1
            line2 = str.split(input_fp2.readline(), ',')

            # Determine whether the number of fields is consistent
            if len(line2) != len(offsets):
                line_error.append(line_count)
            else:
                i = 0
                idx = 0
                for j in offsets:
                    j += i
                    if line2[idx].strip() != line1[i:j].strip():
                        line_error.append(line_count)
                        break
                    i = j
                    idx += 1

            line1 = input_fp1.readline()

        print("Passing rate: {0}/{1}".format((line_count - len(line_error)), line_count))
        if len(line_error):
            print("Error found in line: " + repr(line_error))

        # Determine whether the inputfile2 has extra content
        line2 = input_fp2.readline()
        while line2:
            if line2.strip():
                print("Warning: {0} has extra content".format(input_file2))
                break
            line2 = input_fp2.readline()

    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

    finally:
        if 'confs_fp' in locals():
            confs_fp.close()

        if 'input_fp1' in locals():
            input_fp1.close()

        if 'input_fp2' in locals():
            input_fp2.close()


if __name__ == '__main__':
    main(sys.argv)
