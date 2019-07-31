class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) >= 3:
            result = nums[0]+nums[1]+nums[2]
        else:
            return sum(a)
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                temp_result = nums[i]+nums[j]+nums[k]
                if abs(temp_result-target)<abs(result-target):
                    result = temp_result
                if nums[i]+nums[j]+nums[k] < target:
                    j=j+1
                elif nums[i]+nums[j]+nums[k] == target:
                    return target
                else:
                    k=k-1
        return result

a=Solution()
a.threeSumClosest([-1, 2, 1, -4],1)

