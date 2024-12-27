'''
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

'''
def print_rangoli(size):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    width = 4 * size - 3
    
    #upper pyramid (including middle)
    for i in range(size-1, -1, -1):
        # Get letters from i to size-1
        letters = alpha[i:size]
        # Create palindrome pattern
        row = letters[-1:0:-1] + letters
        # Join with dashes and center
        print('-'.join(row).center(width, '-'))
    
    #bottom pyramid (excluding middle)
    for i in range(1, size):
        letters = alpha[i:size]
        row = letters[-1:0:-1] + letters
        print('-'.join(row).center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)