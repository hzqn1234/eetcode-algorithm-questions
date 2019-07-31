class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        self.get_Combinations('', digits, result)
        return result
    #
    def get_Combinations(self, letters, digits, result):
        if digits == '':
            if letters != '':
                result.append(letters)
        else:
            for letter in self.mapping[digits[0]]:
                self.get_Combinations(letters+letter, digits[1:], result)
    #
    mapping =   {
                    '2': ['a','b','c'],
                    '3': ['d','e','f'],
                    '4': ['g','h','i'],
                    '5': ['j','k','l'],
                    '6': ['m','n','o'],
                    '7': ['p','q','r','s'],
                    '8': ['t','u','v'],
                    '9': ['w','x','y','z']
                }

# slightly faster
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        result = []
        self.get_Combinations('', digits, result)
        return result
    #
    def get_Combinations(self, letters, digits, result):
        if digits == '':
            # if letters != '':
            result.append(letters)
        else:
            for letter in self.mapping[digits[0]]:
                self.get_Combinations(letters+letter, digits[1:], result)
    #
    mapping =   {
                    '2': ['a','b','c'],
                    '3': ['d','e','f'],
                    '4': ['g','h','i'],
                    '5': ['j','k','l'],
                    '6': ['m','n','o'],
                    '7': ['p','q','r','s'],
                    '8': ['t','u','v'],
                    '9': ['w','x','y','z']
                }


a=Solution()
a.letterCombinations('2')
