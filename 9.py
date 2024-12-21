# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command 
# in order and perform the corresponding operation on your list.

# ex:
# N =4
# append 1
# append 2
# insert 3 1
# print

# o/p:
# [1,3,2]
if __name__ == '__main__':
    N = int(input())
    arr=[]
    for _ in range(N):
        command = input().strip().split()
        if command[0] == "insert":
            arr.insert(int(command[1]),int(command[2]))
        if command[0] == "print":
            print(arr)
        if command[0] == "remove":
            arr.remove(int(command[1]))
        if command[0] == "append":
            arr.append(int(command[1]))
        if command[0] == "sort":
            arr.sort()
        if command[0] == "pop":
            arr.pop()
        if command[0] == "reverse":
            arr.reverse()    
