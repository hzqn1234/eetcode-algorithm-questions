# too slow
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        for i in range(0,len(s)):
            temp=""
            for j in range(i,len(s)):
                if s[j] not in temp:
                    temp = temp+s[j]
                else:
                    break
            max_length=max(max_length,len(temp))
        return min(max_length,len(s))

# too slow V2
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        temp_max_length = 0
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                index={}
                temp=""
                temp_max_length = 0
                for k in range(i,j+1):
                    try:
                        index[s[k]]
                        k=j+1
                        break                       
                    except:
                        index[s[k]]=1
                        temp_max_length = temp_max_length + 1
            max_length=max(max_length,temp_max_length)
        return min(max_length,len(s))
      

# too slow V2
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        for i in range(0,len(s)):
            index=[]
            for j in range(i,len(s)):
                if s[j] in index:
                    break
                else:
                    index.append(s[j])
            max_length=max(max_length,len(index))
        return min(max_length,len(s))

# too slow V3
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        for i in range(0,len(s)-1):
            index=set()
            for j in range(i,len(s)):
                if s[j] in index:
                    break
                else:
                    index.add(s[j])
            max_length=max(max_length,len(index))
        return min(max_length,len(s))


# Approach 2: Sliding Window
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        len_s = len(s)
        i=0
        j=0
        set0=set()
        while i <= len_s-1 and j <= len_s-1:
            if s[j] in set0:
                set0.remove(s[i])
                i=i+1
            else:
                set0.add(s[j])
                j=j+1
            max_length=max(max_length,len(set0))
        return max_length

# Approach 3: Sliding Window Optimised
class Solution:
    def lengthOfLongestSubstring(self, s):
        dicts = {}
        maxlength = i = 0
        for j,value in enumerate(s):
            if value in dicts:
                j2 = dicts[value] + 1
                if j2 > i:
                    i = j2
            curr_length = j - i + 1
            if curr_length > maxlength:
                maxlength = curr_length
            dicts[value] = j
        return maxlength



a=Solution()
a.lengthOfLongestSubstring('abcdedf')


