# O(n^2)
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res


# Too slow.. construction of set is O(n), so overall O(n^3)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        dp = set()
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if 0-nums[i]-nums[i+1] < nums[i]:
                break
            for j in range(i+1,len(nums)):
                if (nums[i],nums[j]) in dp:
                    continue
                temp = set(nums[j+1:len(nums)])
                target = 0-nums[i]-nums[j]
                if target in temp:
                    dp.add((nums[i],nums[j]))
                    dp.add((target,nums[j]))
                    dp.add((nums[i],target))
                    ans = [nums[i],target,nums[j]]
                    result.append(ans)
                    # continue
        return result

# O(n^2)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        # dp = set()
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if 0-nums[i]-nums[i+1] < nums[i]:
                break
            j=i+1
            k=len(nums)-1
            while j<k:
                # while (nums[i],nums[j]) in dp and j<k :
                #     j=j+1
                # if j>=k:
                #     break
                if nums[i]+nums[j]+nums[k] < 0
                    j=j+1
                elif nums[i]+nums[j]+nums[k] == 0:
                    # dp.add((nums[i],nums[j]))
                    ans = [nums[i],nums[j],nums[k]]
                    result.append(ans)
                    while j<k and nums[j] == nums[j+1] :
                        j=j+1
                    while j<k and nums[k] == nums[k-1]:
                        k=k-1
                    j=j+1
                else:
                    k=k-1
        return result

a=Solution()
a.threeSum([3,0,-2,-1,1,2])

