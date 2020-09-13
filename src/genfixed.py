#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def gen_fixed(file_name):
    lines = [
        "â"*5 + "ú"*12 + "õ"*3 + "â"*2 + "ú"*13 + "õ"*7 + "â"*10 + "ú"*13 + "õ"*20 + "Ñ"*13 + "\n",
        "â"*5 + "ú"*12 + "õ"*3 + "â"*2 + "ú"*13 + "õ"*7 + "â"*10 + "ú"*13 + "õ"*20 + "Ñ"*13 + "\n",
        "â"*5 + "ú"*12 + "õ"*3 + "â"*2 + "ú"*13 + "õ"*7 + "â"*10 + "ú"*13 + "õ"*20 + "Ñ"*13
    ]
    # print(lines)
    with open(file_name, mode='w', encoding="cp1252") as output_file:
        output_file.writelines(lines)


if __name__ == "__main__":
    gen_fixed('fixed.txt')
