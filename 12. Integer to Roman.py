Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        translate_dict = {	'M'	:	1000,
        					'CM':	900,
        					'D'	:	500,
        					'CD':	400,
        					'C'	:	100,
        					'XC':	90,
        					'L'	:	50,
        					'XL':	40,
        					'X'	:	10,
        					'IX':	9,
        					'V'	:	5,
        					'IV':	4,
        					'I'	:	1
        					}
        result=''
        for l in ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']:
        	while num >= translate_dict[l]:
        		result = result + l
        		num = num - translate_dict[l]
        return result