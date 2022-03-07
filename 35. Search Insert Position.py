# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

# O(n)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        while i < len(nums):
            if nums[i]<target:
                i=i+1
            else:
                return i
        return i


## Binary Search
# O(log(n)) [for input without duplicates]
class Solution:
    def searchInsert(self, nums, target):
        l , r = 0, len(nums)-1
        while l <= r:
            mid=(l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return l


# O(log(n)) [for input with duplicates]
class Solution:
    def searchInsert(self, nums, target): # works even if there are duplicates. 
        l , r = 0, len(nums)-1
        while l <= r:
            mid=int((l+r)/2)
            if nums[mid] < target:
                l = mid+1
            else:
                if nums[mid]== target and nums[mid-1]!=target:
                    return mid
                else:
                    r = mid-1
        return l


