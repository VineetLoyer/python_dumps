# The included code stub will read an integer, , from STDIN.

# Without using any string methods, try to print the following:


# Note that "" represents the consecutive values in between.

# Example
# n=5

# Print the string 12345 .

# Input Format

# The first line contains an integer .

# Constraints
# 1<=n<=150
# Output Format

# Print the list of integers from  through  as a string, without spaces.

if __name__ == '__main__':
    n = int(input())
    print(''.join(str(i+1) for i in range(n)))