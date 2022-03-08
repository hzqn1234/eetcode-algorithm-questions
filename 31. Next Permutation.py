31. Next Permutation
Medium

9051

3060

Add to List

Share
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

## 自己写的，但是用了很多test case，没能自己想到这些test case
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1
        j = n-2
        flag = 0
        while j>=0 and flag == 0:
            while i>j and flag == 0:
                if nums[i]>nums[j]:
                    flag = 1
                    temp = nums[i]
                    ## to-do
                    temp_index = i
                    while temp_index>j:
                        nums[temp_index]=nums[temp_index-1]
                        temp_index=temp_index-1
                    nums[j] = temp
                    ##
                    # j+1->n-1
                    temp_index=j+1
                    while temp_index<n-1:
                        if nums[temp_index]<nums[temp_index+1]:
                            temp = nums[temp_index]
                            nums[temp_index] = nums[temp_index+1]
                            nums[temp_index+1] = temp
                        temp_index = temp_index+1
                    ##
                    temp_index2 = j+1
                    temp_index3 = n-1
                    while temp_index2 < temp_index3:
                        temp = nums[temp_index2]
                        nums[temp_index2] = nums[temp_index3]
                        nums[temp_index3] = temp
                        temp_index2 = temp_index2+1
                        temp_index3 = temp_index3-1
                else:
                    i=i-1
            i=n-1
            j=j-1
        if flag == 0:
            temp_index2 = 0
            temp_index3 = n-1
            while temp_index2 < temp_index3:
                temp = nums[temp_index2]
                nums[temp_index2] = nums[temp_index3]
                nums[temp_index3] = temp
                temp_index2 = temp_index2+1
                temp_index3 = temp_index3-1

## 按标准答案改的 V1
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1
        j = n-2
        flag = 0
        while j>=0 and flag == 0:
            while i>j:
                if nums[i]>nums[j]:
                    flag = 1
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    ##
                    temp_index2 = j+1
                    temp_index3 = n-1
                    while temp_index2 < temp_index3:
                        temp = nums[temp_index2]
                        nums[temp_index2] = nums[temp_index3]
                        nums[temp_index3] = temp
                        temp_index2 = temp_index2+1
                        temp_index3 = temp_index3-1
                    break
                else:
                    i=i-1
            i=n-1
            j=j-1
        if flag == 0:
            temp_index2 = 0
            temp_index3 = n-1
            while temp_index2 < temp_index3:
                temp = nums[temp_index2]
                nums[temp_index2] = nums[temp_index3]
                nums[temp_index3] = temp
                temp_index2 = temp_index2+1
                temp_index3 = temp_index3-1

## 按标准答案改的 V2
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        flag = 0
        i = n-1
        while i>0:
            if nums[i]>nums[i-1]:
                flag = 1
                break
            i=i-1
        if flag == 1:
            i=i-1
            j=i+1
            while j<=n-1:
                if nums[j]<=nums[i]:
                    break
                j=j+1
            j=j-1
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            ##
            temp_index2 = i+1
            temp_index3 = n-1
            while temp_index2 < temp_index3:
                temp = nums[temp_index2]
                nums[temp_index2] = nums[temp_index3]
                nums[temp_index3] = temp
                temp_index2 = temp_index2+1
                temp_index3 = temp_index3-1
        if flag == 0:
            temp_index2 = 0
            temp_index3 = n-1
            while temp_index2 < temp_index3:
                temp = nums[temp_index2]
                nums[temp_index2] = nums[temp_index3]
                nums[temp_index3] = temp
                temp_index2 = temp_index2+1
                temp_index3 = temp_index3-1