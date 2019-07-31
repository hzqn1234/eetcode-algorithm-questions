class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # while len(str)>=1:
        #     if str[0] == ' ':
        #         str=str[1:]
        #     else:
        #         break
        str = str.lstrip()
        sign = 1
        if len(str) == 0:
            return 0
        if str[0] == '-':
            sign = -1
            str = str[1:]
        elif str[0] == '+':
            sign = 1
            str = str[1:]
        i=0
        while len(str)>=1:
            if str[0] == '0':
                str=str[1:]
            else:
                break
        if len(str) == 0:
            return 0
        if not (str[0]>='0' and str[0]<='9'):
            return 0
        i=0
        while i < 12 and i < len(str):
            if not (str[i]>='0' and str[i]<='9'):
                str = str[:i]
                break
            i=i+1
        if (len(str)==10):
            if (sign == -1 and str > '2147483648'):
                return -2147483648
            if (sign == 1 and str > '2147483647'):
                return 2147483647
        if (len(str)>10):
            if (sign == -1):
                return -2147483648
            if (sign == 1):
                return 2147483647        
        result = int(str)*sign   
        return result
