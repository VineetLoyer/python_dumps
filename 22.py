'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size is N X M ( N is odd number and M is 3 times of N)
The design should have 'WELCOME' written in the center.
The design pattern should only use |.. and - characters.

    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
'''

import sys
N,M = map(int,input().split())
# upper pyramid
for i in range(0,N//2):
    pattern = '.|.'*(2*i+1)
    print(pattern.center(M,'-'))
#Welcome part
print('WELCOME'.center(M,'-'))

#Bottom pyramid
for i in range(N//2,0,-1):
    pattern = '.|.'*(2*i-1)
    print(pattern.center(M,'-'))

