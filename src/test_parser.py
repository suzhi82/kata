#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from genfixed import gen_fixed
from parser import intercept, parser


class TestParser(unittest.TestCase):
    def setUp(self):
        print("\nTesting", self.id())

    def tearDown(self):
        print("*"*60)

    # generate fixed width file test
    def test_gen_fixed(self):
        lines1 = [
            "â" * 5 + "ú" * 12 + "õ" * 3 + "â" * 2 + "ú" * 13 + "õ" * 7 + "â" * 10 + "ú" * 13 + "õ" * 20 + "Ñ" * 13 + "\n",
            "â" * 5 + "ú" * 12 + "õ" * 3 + "â" * 2 + "ú" * 13 + "õ" * 7 + "â" * 10 + "ú" * 13 + "õ" * 20 + "Ñ" * 13 + "\n",
            "â" * 5 + "ú" * 12 + "õ" * 3 + "â" * 2 + "ú" * 13 + "õ" * 7 + "â" * 10 + "ú" * 13 + "õ" * 20 + "Ñ" * 13
        ]
        file_name = 'fixed.txt'
        gen_fixed(file_name)
        with open(file_name, mode='r', encoding='cp1252') as f:
            lines2 = f.readlines()
        self.assertEqual(lines1, lines2)

    # intercept string test
    def test_intercept(self):
        line = "ABBCCCDDDD"
        pos = [1, 2, 3, 4]
        self.assertEqual(intercept(line, pos), ['A', 'BB', 'CCC', 'DDDD'])

    # input non-exist file test
    def test_parser_non_exist_file(self):
        with self.assertRaises(FileNotFoundError):
            parser('file1', 'file2', 'file3')

    # compare the content of fixed width file and delimited file test
    def test_parser_content(self):
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
