'''
The first line contains integer , the number of elements in the set .
The second line contains  space separated elements of set . All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer , the number of commands.
The next  lines contains either pop, remove and/or discard commands followed by their associated value.

Output:
Print the sum of the elements of set  on a single line.

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

4
'''
n = int(input())
s = set(map(int, input().split()))
c = int(input())
for i in range(c):
    com = list(input().split())
    if com[0]=='pop':
        s.pop()
    if com[0]=='remove':
        s.remove(int(com[1]))
    if com[0]=='discard':
        s.discard(int(com[1]))

sum1=0
for n in s:
    sum1+=n

print(sum1)
