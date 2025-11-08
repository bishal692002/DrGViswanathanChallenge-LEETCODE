class Solution(object):
    def secondHighest(self, s):
        list = []
        for char in s:
            if char.isdigit() and char not in list:
                list.append(char)
        list.sort()
        if len(list) <= 1:
            return -1
        else:
            return int(list[-2])
