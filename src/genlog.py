#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import sys


def main():
    confs_file = 'spec.json'
    output_file = 'test.log'
    line_count = 100
    schar = 'á'

    try:
        json_fp = open(confs_file, mode='r')
        confs = json.load(json_fp)

        fields = list(map(lambda x: '%' + x + 's', confs['Offsets']))
        print(fields)

        line_str = ''
        for f in fields:
            line_str += f % schar
        line_str += '\n'

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
        if 'json_fp' in dir():
            json_fp.close()

        if 'output_fp' in dir():
            output_fp.flush()
            output_fp.close()


if __name__ == '__main__':
    main()
