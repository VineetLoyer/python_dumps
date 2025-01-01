'''
The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
Explanation

You gain 1 unit of happiness for elements 3 and  1 in set . You lose 1 unit for 5 in set . The element 7 in set B does not exist in the array so it is not included in the calculation.

Hence, the total happiness is .
'''
from collections import Counter

# Read n and m
n, m = map(int, input().split())

# Read the array
arr = list(map(int, input().split()))

# Count occurrences of elements in the array
arr_count = Counter(arr)

# Read sets A and B
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# Calculate happiness directly
happiness = sum(arr_count[num] for num in A if num in arr_count) - sum(arr_count[num] for num in B if num in arr_count)

# Print total happiness
print(happiness)

