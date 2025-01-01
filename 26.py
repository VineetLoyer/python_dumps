'''
Function Description

Complete the average function in the editor below.

average has the following parameters:

int arr: an array of integers
Returns
float: the resulting float value rounded to 3 places after the decimal
Input Format

The first line contains the integer,N , the size of arr.
The second line contains the N space-separated integers, arr[i].
'''

def average(array):
    s = set(array)
    su = sum(s)
    l = len(s)
    return su/l

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)