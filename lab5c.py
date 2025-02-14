#!/usr/bin/env python3
# Author ID: rnagarasa

def add(number1, number2):
    try:
        return int(number1) + int(number2)
    except ValueError:
        return 'error: could not add numbers'

def read_file(filename):
    try:
        f = open(filename, 'r')
        file_data = f.readlines()
        f.close()
        return file_data
    except FileNotFoundError:
        return'error: could not read file'


if __name__ == '__main__':
    print(add(10, 5))
    print(add('10', 5))
    print(add('abc', 5))
    print(read_file('seneca2.txt'))
    print(read_file('file10000.txt'))