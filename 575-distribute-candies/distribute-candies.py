class Solution(object):
    def distributeCandies(self, candyType):
        candyTypeSet = set(candyType)

        n1 = len(candyType)/2
        n2 = len(candyTypeSet) 

        if n2 > n1:
            return n1

        return n2
                
       