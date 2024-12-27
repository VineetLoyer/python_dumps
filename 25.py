# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


import os


def solve(s):
    for i in range(len(s)):
        if i == 0 or s[i-1] == ' ':
            s = s[:i] + s[i].upper() + s[i+1:]
    return s
   
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()