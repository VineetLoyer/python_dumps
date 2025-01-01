'''
Input Format

The first line contains an integer , the total number of country stamps.
The next N lines contains the name of the country where the stamp is from.

Constraints


Output Format

Output the total number of distinct country stamps on a single line.

Sample Input

7
UK
China
USA
France
New Zealand
UK
France 
Sample Output

5
'''

a = int(input())
arr=[]
for i in range(a):
    coun = input()
    arr.append(coun)

print(len(set(arr)))