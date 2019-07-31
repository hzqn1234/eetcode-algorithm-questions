class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            sign = -1
            x = x * -1
        else:
            sign = 1
        s   = str(x)
        s2  = ''
        l   = len(s)
        for i in range(l):
            s2=s2+s[l-1-i]
        if len(s2) > 10:
            return 0
        if (len(s2) == 10) and ((sign == -1 and s2 > '2147483648') or (sign == 1 and s2 > '2147483647')):
            return 0
        result = int(s2)*sign       
        return result