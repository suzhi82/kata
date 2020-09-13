#!/usr/bin/env python3
# -*- coding: utf-8 -*-


lines = [
    "â"*5 + "ú"*12 + "õ"*3 + "â"*2 + "ú"*13 + "õ"*7 + "â"*10 + "ú"*13 + "õ"*20 + "Ñ"*13 + "\n",
    "â"*5 + "ú"*12 + "õ"*3 + "â"*2 + "ú"*13 + "õ"*7 + "â"*10 + "ú"*13 + "õ"*20 + "Ñ"*13 + "\n",
    "â"*5 + "ú"*12 + "õ"*3 + "â"*2 + "ú"*13 + "õ"*7 + "â"*10 + "ú"*13 + "õ"*20 + "Ñ"*13
]

print(lines)

with open('fixed.txt', mode='w', encoding="cp1252") as output_file:
    output_file.writelines(lines)

