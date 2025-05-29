class Solution(object):
    def canWinNim(self, n):
       if n==1:
          return True
       elif n==2:
          return True
       else:
          return n%4!=0