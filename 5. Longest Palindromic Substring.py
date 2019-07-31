Palindromic 回文结构的

# Too slow
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        l=len(s)
        max_substring_len=0
        max_substring=''
        for i in range(0,l):
            for j in range(i,l):
                check=0
                for k in range(i,(i+j-1)/2+1):
                    if s[k] != s[i+j-k]:
                        check=1
                        break
                if check == 0 and j-i+1 > max_substring_len:
                    max_substring_len = j-i+1
                    max_substring = s[i:j+1]
        return max_substring


# a bit slow, dynamic programming (recursion)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        l=len(s)
        marks=[[None]*l for i in range(0,l)]
        max_substring_len=0
        max_substring=''
        for i in range(0,l):
            marks[i][i] = True
        for i in range(0,l-1):
            marks[i][i+1] = (s[i] == s[i+1])
        for i in range(0,l):
            for j in range(i,l):
                if (j-i+1 > max_substring_len) and self.is_Palindrome(s,i,j,marks):
                    max_substring_len = j-i+1
                    max_substring = s[i:j+1]
                    
        return max_substring

    def is_Palindrome(self,s,i,j,marks):
        marks[i][j] = ((marks[i][j]) or (s[i] == s[j])) and ((j-i<2) or (marks[i+1][j-1] or self.is_Palindrome(s,i+1,j-1,marks)))
        return marks[i][j]


# Accepted, Expand Around Center
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        l=len(s)
        marks=[[None]*l for i in range(0,l)]
        max_substring_len=0
        max_substring=''
        # start with 1 char
        for i in range(0,l):
            ia=ib=i
            flag = True
            while ia>=0 and ib <= l-1 and flag == True:
                if s[ia]==s[ib]:
                    if ib-ia+1 > max_substring_len:
                        max_substring_len = ib-ia+1
                        max_substring = s[ia:ib+1]
                    ia=ia-1
                    ib=ib+1
                else:
                    flag = False

        # start with 2 char
        for i in range(0,l-1):
            ia=i
            ib=i+1
            flag = True
            while ia>=0 and ib <= l-1 and flag == True:
                if s[ia]==s[ib]:
                    if ib-ia+1 > max_substring_len:
                        max_substring_len = ib-ia+1
                        max_substring = s[ia:ib+1]
                    ia=ia-1
                    ib=ib+1
                else:
                    flag = False
                    
        return max_substring


