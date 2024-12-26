'''
String split and join

ip: this is a string 
op: this-is-a-string
'''

def split_and_join(line):
    # write your code here
    line = line.split(' ')
    line = '-'.join(line)
    return line