'''
Given an integer,n , and  space-separated integers as input, create a tuple,t , of those  integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer, , denoting the number of elements in the tuple.
The second line contains  space-separated integers describing the elements in tuple .

Output Format

Print the result of .
'''

#used PyPy3 since the test cases use the same, Py3 randomize the hash values for security reasons so get different output in different sesisons.

if __name__ == '__main__':
    n = int(input())  # Read the number of elements
    # t = []
    # e = input().split()
    # for i in range(n):
    #     t.append(int(e[i]))
    
    # t = tuple(t)
    # print(hash(t))
    t = tuple(map(int,input().split()))
    print(hash(t))
    