# Recursion, Slow, but accepted :)
class Solution(object):
    def isMatch(self, s, p, p_pre=None):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        print ("s='%s',p='%s',p_pre='%s'" % (str(s),str(p),str(p_pre)))
        if len(s)==0:
            if len(p)==0:
                return True
            elif len(p)>=1 and p[0] == '*':
                return self.isMatch(s[:],p[1:],p_pre=p_pre)
            elif len(p)>=2 and p[1] == '*':
                return self.isMatch(s[:],p[2:],p_pre=p_pre)
            else:
                return False
        else:
            if len(p)==0:
                return False
            else:
                pass
        #
        result = False
        #
        if (s[0] == p[0] or p[0] =='.'):
            result = self.isMatch(s[1:],p[1:],p_pre=p[0])
            if result == True:
                return True
        # print '1'
        #
        if (s[0] == p_pre or p_pre =='.') and p[0] == '*':
            result = self.isMatch(s[1:],p[:],p_pre=p_pre)
            if result == True:
                return True
        # print '2'
        #
        if len(p)>=2 and p[1] == '*':
            result = self.isMatch(s[:],p[2:],p_pre=p_pre)
            if result == True:
                return True
        # print '3'
        #
        if p[0] == '*':
            result = self.isMatch(s[:],p[1:],p_pre=p_pre)
            if result == True:
                return True
        return result


# Recursion standard anwser, also quite slow, but faster and cleaner than above solution
class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


# dynamic programming solution
class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)



a = Solution()



a.isMatch('asd','asd')
a.isMatch('aasd','a*sd')
a.isMatch('aasd','.*sd')
a.isMatch('aasd','.*')
a.isMatch('sd','*sd')
a.isMatch('','*')
a.isMatch('','c*c*')
a.isMatch('abbabaaaaaaacaa',"a*.*b.a.*c*b*a*c*")
a.isMatch('','*c*b*a*c*')
s='',p='*c*b*a*c*',p_pre='.'