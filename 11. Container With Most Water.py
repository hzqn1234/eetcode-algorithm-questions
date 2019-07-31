# O(n), accepted, (Two Pointer Approach, code simplified)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_vol 	= 0
        length 		= len(height)
        left_index 	= 0
        right_index = length - 1
        while left_index <= right_index:
        	max_vol = max(max_vol,(min(height[left_index],height[right_index])*(right_index-left_index)))
        	if height[left_index] >= height[right_index]:
        		right_index = right_index - 1
        	else:
        		left_index = left_index + 1
        return max_vol

# O(n), accepted, (Two Pointer Approach)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_vol 	= 0
        length 		= len(height)
        left_index 	= 0
        right_index = length - 1
        left 		= height[left_index]
        right 		= height[right_index]
        while left_index <= right_index:
        	max_vol = max(max_vol,(min(left,right)*(right_index-left_index)))
        	if left >= right:
        		right_index = right_index - 1
        		right 		= height[right_index]
        	else:
        		left_index = left_index + 1
        		left 		= height[left_index]
        return max_vol


# O(n^2) with max_left & max_right optimisation, still too slow
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_vol = 0
        max_left = 0
        length = len(height)
        for i in range(0,length-1):
        	if height[i] > max_left:
        		max_left = height[i]
        		max_right = 0
	        	for j in reversed(range(i,length)):
	        		if height[j] > max_right:
	        			max_right = height[j]
		        		temp_vol = min(height[i],height[j])*(j-i)
		        		max_vol = max(max_vol,temp_vol)
        return max_vol


# O(n^2) with max_left optimisation, still too slow
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_vol = 0
        max_left = 0
        length = len(height)
        for i in range(0,length-1):
        	if height[i] > max_left:
        		max_left = height[i]
	        	for j in range(i,length):
	        		temp_vol = min(height[i],height[j])*(j-i)
	        		max_vol = max(max_vol,temp_vol)
        return max_vol


# O(n^2), too slow
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_vol = 0
        length = len(height)
        for i in range(0,length-1):
        	for j in range(i,length):
        		temp_vol = min(height[i],height[j])*(j-i)
        		max_vol = max(max_vol,temp_vol)
        return max_vol









