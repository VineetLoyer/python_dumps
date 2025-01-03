'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2 
'''
def swap_case(s):
    s = s.swapcase()
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


#without using swapcase function

def swap_case(s):
    result = ''
    if chr in s:
        if chr.isupper():
            result+=chr.lower()
        elif chr.islower():
            result+=chr.upper()
        else:
            result+=chr
    return chr