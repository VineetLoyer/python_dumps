'''
Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

Input Format

The first line of input contains an integer,M .
The second line contains M space-separated integers.
The third line contains an integer,N .
The fourth line contains N space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}
Sample Output

5
9
11
12
'''
n1 = int(input())
arr1 = list(map(int, input().split()))
n2= int(input())
arr2 = list(map(int, input().split()))
res = sorted(set(arr1).symmetric_difference(set(arr2)))
for n in res:
    print(n)