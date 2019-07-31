# convert to string
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        for i in range(len(x)/2):
            if x[i] != x[len(x)-1-i]:
                return False
        return True


# not convert to string
import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x==0:
            return True
        i=0
        while math.log10(x)/2 >= i:
            a = x/(10**i)%10
            b = x/(10**(int(math.log10(x))-i))%10
            if a != b :
                return False
            i = i + 1
        return True


