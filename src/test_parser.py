#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from genfixed import gen_fixed
from parser import intercept, parser


class TestParser(unittest.TestCase):

    # input non-exist file test
    def test_case01(self):
        with self.assertRaises(FileNotFoundError):
            parser('file1', 'file2', 'file3')

    # intercept string test
    def test_case02(self):
        line = "ABBCCCDDDD"
        pos = [1, 2, 3, 4]
        self.assertEqual(intercept(line, pos), ['A', 'BB', 'CCC', 'DDDD'])

    # generate fixed width file test
    def test_case03(self):
        lines1 = [
            "â" * 5 + "ú" * 12 + "õ" * 3 + "â" * 2 + "ú" * 13 + "õ" * 7 + "â" * 10 + "ú" * 13 + "õ" * 20 + "Ñ" * 13 + "\n",
            "â" * 5 + "ú" * 12 + "õ" * 3 + "â" * 2 + "ú" * 13 + "õ" * 7 + "â" * 10 + "ú" * 13 + "õ" * 20 + "Ñ" * 13 + "\n",
            "â" * 5 + "ú" * 12 + "õ" * 3 + "â" * 2 + "ú" * 13 + "õ" * 7 + "â" * 10 + "ú" * 13 + "õ" * 20 + "Ñ" * 13
        ]
        file_name = 'fixed.txt'
        gen_fixed(file_name)
        with open(file_name, mode='r', encoding='cp1252') as f:
            lines2 = []
            line = f.readline()
            while line:
                lines2.append(line)
                line = f.readline()
        self.assertEqual(lines1, lines2)

    # compare the content of fixed width file and delimited file
    def test_case04(self):
        include_header = True

        with open('fixed.txt', mode='r', encoding='cp1252') as file1, \
                open('delim.csv', mode='r', encoding='utf-8') as file2:
            if include_header:
                file2.readline()
            line1 = file1.readline()
            line2 = file2.readline()
            while line1 or line2:
                self.assertEqual(line1.strip('\n'), line2.strip('\n').replace(',', ''))
                line1 = file1.readline()
                line2 = file2.readline()


if __name__ == "__main__":
    unittest.main()
