class Solution(object):
    def compareVersion(self, version1, version2):
        list1 = map(int,version1.split("."))
        list2 = map(int,version2.split("."))

        for i in range(max(len(list1),len(list2))):
            value1 = list1[i] if i < len(list1) else 0
            value2 = list2[i] if i < len(list2) else 0

            if value1 < value2:
                return -1

            if value1 > value2:
                return 1

        return 0