#!/usr/bin/env python3
# Author ID: rnagarasa

def read_file_string(file_name):
    f = open(file_name, 'r')
    file_data = f.read()
    f.close()
    return file_data


def read_file_list(file_name):
    f = open(file_name, 'r')
    file_data = [line[:-1] for line in list(f)]
    f.close()
    return file_data




if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))