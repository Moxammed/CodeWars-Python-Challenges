'''
------Instructions------
Description:
Remove all exclamation marks from the end of sentence.

Examples
"Hi!"     ---> "Hi"
"Hi!!!"   ---> "Hi"
"!Hi"     ---> "!Hi"
"!Hi!"    ---> "!Hi"
"Hi! Hi!" ---> "Hi! Hi"
"Hi"      ---> "Hi"


------Solution------
'''
def remove(st):
    length= len(st)
    for i in range(length-1, -1, -1):
        if st[i]=='!':
            st = st[:i] # OR        st = st[:-1]
        else:
            return st
            
    return st



'''
Solution 2

def remove(st):
    while st.endswith('!'):
        st = st[:-1]
    return st
'''