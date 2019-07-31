class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        result = ''
        n = len(strs)
        if n == 0:
            return ''
        i = 0
        flag = True
        while flag:
            if i < len(strs[0]):
                s = strs[0][i]
                for j in range(1,n):
                    if i >= len(strs[j]) or s != strs[j][i]:
                        flag = False
                if flag:
                    result = result + s
                    i = i + 1
            else:
                flag = False
        return result