# ex:
# x=1
# y=1
# z=2
# n=3

# print all permutations of [i,j,k] such that i+j+k!=n, use list comprehension

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    cor = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
    print(cor)