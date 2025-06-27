class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        final_list=[]
        def backtrack(cur_str,open_count,close_count):
            if open_count==n and close_count ==n:
                final_list.append(cur_str)
                return
            if close_count < open_count:
                backtrack(cur_str+")",open_count,close_count+1)
            if  open_count<n: 
                backtrack(cur_str+"(",open_count+1,close_count)
        backtrack("(",1,0)
        return final_list