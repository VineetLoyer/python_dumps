'''
Sample Input

 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66

Sample Output

38

'''
n = int(input())
arr1 =set(map(int,input().split()))
c= int(input())
for i in range(c):
    com = list(input().split())
    if(com[0]=='intersection_update'):
        arr2 = set(map(int,input().split()))
        arr1.intersection_update(arr2)
    if (com[0]=='update'):
        arr3 = set(map(int,input().split()))
        arr1.update(arr3)
    if (com[0]=='difference_update'):
        arr4 = set(map(int,input().split()))
        arr1.difference_update(arr4)
    if (com[0]=='symmetric_difference_update'):
        arr5 = set(map(int,input().split()))
        arr1.symmetric_difference_update(arr5)

sum1=0
for n in arr1:
    sum1+=n
    
print(sum1)
