# accepted
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {'{':'}','(':')','[':']'}
        for i in s:
            if i in ('{','[','('):
                stack.append(i)
            elif not stack or mapping[stack.pop()] != i:
                return False
        if len(stack) == 0:
            return True
        else:
            return False


# slightly faster
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {'{':'}','(':')','[':']'}
        i = 0
        while i < len(s):
            if s[i] in ('{','[','('):
                i=i+1
            else:
                if i>=1 and mapping[s[i-1]] == s[i]:
                    s = s[:i-1]+s[i+1:]
                    i = i-1
                else:
                    return False
        if s == '':
            return True
        else:
            return False
