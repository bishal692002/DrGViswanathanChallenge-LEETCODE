class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s    
        st=[]
        for i in range(numRows):
            st.append("")
        k=0
        for i in range(len(s)):
            if i==0:
                st[0]=st[0]+s[0]
            else:    
                j=int((i-1)/(numRows-1))
                if j%2==0:
                    k=k+1
                else:
                    k=k-1    
                st[k]=st[k]+s[i]
        z=[""]       
        for i in range(numRows):
            for j in range(len(st[i])):
                z[0]=z[0]+st[i][j]    
        return z[0]



            


        