class Solution(object):
    def reverse(self, x):
        st= str(x)
        l= []
        r= []
        for i in st:
            l.append(i)
        for i in l:
            r.insert(0,i)
        s=""
        for i in r:
            s+=i
        if s[-1]== '-':
            s= s[:-1]
            s= '-' + s
        ans= int(s)
        
        if ans> 2**31-1 or ans< -2**31:
            return 0
        else: 
            return ans