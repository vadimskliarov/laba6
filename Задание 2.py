#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# создайте словарь, где ключами являются числа, а значениями – строки.
# Примените к нему метод items(), c с помощью полученного объекта dict_items создайте
# новый словарь, "обратный" исходному, т. е. ключами являются строки, а значениями –
# числа.
from datetime import date
import sys

if __name__ == '__main__':
    list_1 = {3: 'three', 5: 'five', 2: 'two'}
    list_2 = dict(map(reversed, list_1.items()))

    print(list_1)
    print(list_2)