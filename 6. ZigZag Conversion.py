class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l = ['' for i in range(numRows)]
        # c = 0
        r = 0
        direction = 0
        count = 0
        max_count=len(s)
        while count < max_count:
            l[r] = l[r] + s[count]
            if direction == 0:
                if r < numRows-1:
                    r = r + 1
                else:
                    r = r - 1
                    # c = c + 1
                    direction = 1
            else:
                if r > 0:
                    r = r - 1
                else:
                    r = r + 1
                    # c = c + 1
                    direction = 0
            count = count + 1
        #
        result=''
        for i in range(numRows):
            result = result + l[i]
        return result

a=Solution()
print a.convert("PAYPALISHIRING",3)

