class Solution(object):
    dp = {1:['()'],2:['()()','(())']}
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.sub_gen(n)
        return list(set(self.dp[n]))
    #
    def sub_gen(self, n):
        if n in self.dp:
            return self.dp[n]
        if n not in self.dp:
            temp_list = []
            for i in range(1,n):
                for item1 in self.sub_gen(i):
                    for item2 in self.sub_gen(n-i):
                        temp_list.append(item1+item2)
            for item in self.sub_gen(n-1):
                temp_list.append('('+item+')')
            self.dp.update({n:temp_list})
        return self.dp[n]

a = Solution()
a.generateParenthesis(3)
