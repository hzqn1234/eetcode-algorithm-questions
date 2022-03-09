32. Longest Valid Parentheses
Hard

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.


## 勉强够快。。。
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n=len(s)
        if n == 0:
            return 0
        best = 0
        i = 0
        while i<n-1:
            count = 0
            j=i
            new_i=i
            leftcount_min=0
            left_flag=0
            while j<=n-1 and count>=0:
                if s[j]=='(':
                    count=count+1
                    if left_flag==0:
                        leftcount_min = count
                else:
                    left_flag=1
                    count=count-1
                    if count<leftcount_min:
                        leftcount_min = count
                temp = j-i+1
                if count == 0:
                    new_i=j
                    if temp>best:
                        best = temp                
                j=j+1
            i=new_i+max(leftcount_min,1)
        return best


## dynamic programming, 太慢
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n=len(s)
        if n == 0:
            return 0
        
        data        = dict()
        check       = dict()
        valid       = dict()

        def get_valid(i,j):
            if (i,j) not in valid:
                valid[(i,j)] = get_data(i,j)*2 == (j-i+1)
            return valid[(i,j)]
                      
        def get_check(i,j):
            if (i,j) not in check:
                check[(i,j)]=(s[i]=='(')*(s[j]==')')
            return check[(i,j)]

        def get_data(i,j):
            if (i,j) not in data:
                if j-i==1:
                    data[(i,j)] = get_check(i,j)
                elif j-i<=0:
                    data[(i,j)] = 0
                else:
                    temp_max = get_data(i+1,j-1)*get_valid(i+1,j-1) + get_check(i,j)
                    for index in range(j-i):
                        index2=i+index
                        temp = get_data(i,index2)*get_valid(i,index2) + get_data(index2+1,j)*get_valid(index2+1,j)
                        if temp>temp_max:
                            temp_max=temp
                    data[(i,j)] = temp_max
            return data[(i,j)]
        get_data(0,len(s)-1)
        return max(data.values())*2








