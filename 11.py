'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains n . The second line contains an array A[]  of n integers each separated by a space.

Output format

Print runner up score

5
2 3 6 6 5

o/p : 5
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(arr) #O(nlogn)
    hashset = []
    for i in range(len(arr)): #O(n)
        if arr[i] not in hashset:
            hashset.append(arr[i])
        else:
            continue
    
    print(hashset[-2])

   # O(n) + O(nlogn)

# Better approach - converting the arr to set then use sorted function on s which gives a list

    s = set(arr) 
    l = sorted(s)  #O(nlogn)
    print(l[-2])

    # O(nlogn) 