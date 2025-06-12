class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        value = 0
        for i in range(len(operations)):
            ip = operations[i]
            if ip == "--X" or ip == "X--":
                value -= 1
            
            elif ip == "++X" or ip=="X++":
                value += 1
        return value