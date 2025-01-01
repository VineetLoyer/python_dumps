'''
Input Format

The first line contains an integer,m , the number of students who have subscribed to the English newspaper.
The second line contains m  space separated roll numbers of those students.
The third line contains  b, the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students.

Output total number of students who have subscriptions to the English or the French newspaper but not both.
'''
a = int(input())
arr1 = set(map(int,input().split()))
b = int(input())
arr2=set(map(int,input().split()))
arr3 = arr1.symmetric_difference(arr2)
print(len(arr3))