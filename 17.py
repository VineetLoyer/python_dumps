'''
String mutations
STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'
'''
def mutate_string(string, position, character):
    n = list(string)
    n[position]=character
    st =''.join(n)
    
    return st

#another approach 
def mutate_string(string, position, character):
    st = string[:position] +character+string[position+1:]
    return st