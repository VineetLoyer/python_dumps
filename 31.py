'''
Input Format

The first line contains an integer,n , the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students.


Output the total number of students who have at least one subscription.
'''
a = int(input())
arr1 = set(map(int,input().split()))
b = int(input())
arr2=set(map(int,input().split()))
arr3 = arr1.union(arr2)
print(len(arr3))