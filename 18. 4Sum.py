# Slow, but accepted
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        length = len(nums)
        if length < 4:
            return []
        nums.sort()
        i=0
        while i < length-3:
            j=i+1
            while j < length-2:
                k = j+1
                l = length-1
                while k<l:
                    if nums[i]+nums[j]+nums[k]+nums[l] < target:
                        k=k+1
                    elif nums[i]+nums[j]+nums[k]+nums[l] == target:
                        result.append([nums[i],nums[j],nums[k],nums[l]])
                        k=k+1
                        while nums[k] == nums[k-1] and k < l:
                            k=k+1
                    else:
                        l=l-1
                        while nums[l] == nums[l+1] and k < l:
                            l=l-1
                j=j+1
                while nums[j] == nums[j-1] and j < length-2:
                    j=j+1
            i=i+1
            while nums[i] == nums[i-1] and i < length-3:
                i=i+1 
        return result

# Optimisation of the above solution
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        length = len(nums)
        if length < 4:
            return []
        nums.sort()
        i=0
        while i < length-3:
            j=i+1
            if nums[i]+3*nums[j]>target:
                break
            while j < length-2:
                k = j+1
                l = length-1
                if nums[i]+nums[j]+2*nums[k]>target:
                        break
                while k<l:
                    if nums[i]+nums[j]+2*nums[k]>target or nums[i]+nums[j]+2*nums[l]<target:
                        break
                    if nums[i]+nums[j]+nums[k]+nums[l] < target:
                        k=k+1
                    elif nums[i]+nums[j]+nums[k]+nums[l] == target:
                        result.append([nums[i],nums[j],nums[k],nums[l]])
                        k=k+1
                        while nums[k] == nums[k-1] and k < l:
                            k=k+1
                    else:
                        l=l-1
                        while nums[l] == nums[l+1] and k < l:
                            l=l-1
                j=j+1
                while nums[j] == nums[j-1] and j < length-2:
                    j=j+1
            i=i+1
            while nums[i] == nums[i-1] and i < length-3:
                i=i+1 
        return result

# Fast solution, reduce 4-sum to 2-sum
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2: return

        # solve 2-sum
        if N == 2:
            l,r = 0,len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums)-N+1):   # careful about range
                if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                    self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        return



a=Solution()
a.fourSum([-7,-5,0,7,1,1,-10,-2,7,7,-2,-6,0,-10,-5,7,-8,5],28)
