
def count_substring(string, sub_string):
    count = 0
    l1 = len(string)
    l2 = len(sub_string)
    print("lenght of string ",l1)
    print("length of sub_string ",l2)
    
    for i in range(0,l1-l2+1):
        if string[i:i+l2] == sub_string:
            print(string[i:i+l2])
            count+=1
    return count

if __name__ == '__main__':
    string = 'abcdcdc'
    sub_string = 'cdc'
    
    count = count_substring(string, sub_string)
    print(count)
