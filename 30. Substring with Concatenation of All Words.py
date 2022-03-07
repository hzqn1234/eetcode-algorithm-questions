# 30. Substring with Concatenation of All Words
# Hard

# You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.
# You can return the answer in any order.

# Example 1:

# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
# Example 2:

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
# Example 3:

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lower-case English letters.
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# words[i] consists of lower-case English letters.


## 自己写的，慢是慢了点，但是能pass...
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def findSubstring_by_index(s,words):
            word_len = len(words[0])
            s_word_0 = s[0:word_len]
            if s_word_0 not in words:
                return 0
            else:
                words_temp = words.copy()
                words_temp.remove(s_word_0)
                if len(words_temp) == 0:
                    return 1
                else:
                    return findSubstring_by_index(s[word_len:],words_temp)

        result = []
        len_s = len(s)
        word_len = len(words[0])
        words_count = len(words)
        for index in range(len_s):
            if len_s - index >= word_len * words_count:
                if findSubstring_by_index(s[index:],words) == 1:
                    result.append(index)
        return result


## 自己写的优化版
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def findSubstring_by_index(s,words):
            word_len = len(words[0])
            s_word_0 = s[0:word_len]
            if s_word_0 not in words:
                return 0
            else:
                words_temp = words.copy()
                words_temp.remove(s_word_0)
                if len(words_temp) == 0:
                    return 1
                else:
                    return findSubstring_by_index(s[word_len:],words_temp)

        result = []
        len_s = len(s)
        word_len = len(words[0])
        words_count = len(words)
        target_len = word_len * words_count
        for index in range(len_s-target_len+1):
            if findSubstring_by_index(s[index:index+target_len-1],words) == 1:
                result.append(index)
        return result


# 标准答案
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = collections.Counter(words)
        
        def sliding_window(left):
            words_found = collections.defaultdict(int)
            words_used = 0
            excess_word = False
            
            # Do the same iteration pattern as the previous approach - iterate
            # word_length at a time, and at each iteration we focus on one word
            for right in range(left, n, word_length):
                if right + word_length > n:
                    break

                sub = s[right : right + word_length]
                if sub not in word_count:
                    # Mismatched word - reset the window
                    words_found = collections.defaultdict(int)
                    words_used = 0
                    excess_word = False
                    left = right + word_length # Retry at the next index
                else:
                    # If we reached max window size or have an excess word
                    while right - left == substring_size or excess_word:
                        # Move the left bound over continously
                        leftmost_word = s[left : left + word_length]
                        left += word_length
                        words_found[leftmost_word] -= 1

                        if words_found[leftmost_word] == word_count[leftmost_word]:
                            # This word was the excess word
                            excess_word = False
                        else:
                            # Otherwise we actually needed it
                            words_used -= 1
                    
                    # Keep track of how many times this word occurs in the window
                    words_found[sub] += 1
                    if words_found[sub] <= word_count[sub]:
                        words_used += 1
                    else:
                        # Found too many instances already
                        excess_word = True
                    
                    if words_used == k and not excess_word:
                        # Found a valid substring
                        answer.append(left)
        
        answer = []
        for i in range(word_length):
            sliding_window(i)

        return answer
