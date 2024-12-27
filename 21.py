'''
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w .

ex:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

'''

import textwrap

def wrap(string, max_width):
    wrapper=textwrap.TextWrapper(width=max_width)
    st = wrapper.fill(text=string) 
    return st
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
