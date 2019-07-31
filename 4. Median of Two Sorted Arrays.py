# Passed
import bisect
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        print nums1, nums2
        print len(nums1),len(nums2)
        smaller_len = min(len(nums1),len(nums2))
        if len(nums1)+len(nums2) == 1:
            return sum(nums1)+sum(nums2)
        #
        if len(nums1) == 0:
            print 'in 1'
            return self.find_median(nums2)
        #
        if len(nums2) == 0:
            print 'in 2'
            return self.find_median(nums1)
        #
        if len(nums1) == 1:
            print 'in 3'
            bisect.insort(nums2, nums1[0])
            return self.find_median(nums2)
        #
        if len(nums2) == 1:
            print 'in 4'
            bisect.insort(nums1, nums2[0])
            return self.find_median(nums1)
        #
        if len(nums1) == 2:
            print 'in 5'
            bisect.insort(nums2, nums1[0])
            bisect.insort(nums2, nums1[1])
            return self.find_median(nums2)
        #
        if len(nums2) == 2:
            print 'in 6'
            bisect.insort(nums1, nums2[0])
            bisect.insort(nums1, nums2[1])
            return self.find_median(nums1)
        if nums1[-1] <= nums2[0]:
            print 'in 7'
            return self.find_median(nums1 + nums2)
        #
        if nums2[-1] <= nums1[0]:
            print 'in 8'
            return self.find_median(nums2 + nums1)
        #
        median1 = self.find_median(nums1)
        median2 = self.find_median(nums2)
        if median1 < median2:
            print 'in 9'
            return self.findMedianSortedArrays(nums1[(smaller_len-1)//2:], nums2[:(len(nums2)) - (smaller_len-1)//2])
        elif median1 == median2:
            print 'in 10'
            return median1
        else:
            print 'in 11'
            return self.findMedianSortedArrays(nums2[(smaller_len-1)//2:], nums1[:(len(nums1)) - (smaller_len-1)//2]) 
    #
    def find_median(self,a):
        if len(a) % 2 ==0:
            return (a[len(a)//2]+a[len(a)//2-1]) / 2.0
        else:
            return a[len(a)//2]

# Optimised
import bisect
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > 2 and len(nums2) > 2:
            print nums1, nums2
            print len(nums1),len(nums2)
            smaller_len = min(len(nums1),len(nums2))
            # if len(nums1)+len(nums2) == 1:
            #     return sum(nums1)+sum(nums2)
            #
            if nums1[-1] <= nums2[0]:
                print 'in 7'
                return self.find_median(nums1 + nums2)
            #
            if nums2[-1] <= nums1[0]:
                print 'in 8'
                return self.find_median(nums2 + nums1)
            #
            median1 = self.find_median(nums1)
            median2 = self.find_median(nums2)
            if median1 < median2:
                print 'in 9'
                return self.findMedianSortedArrays(nums1[(smaller_len-1)//2:], nums2[:(len(nums2)) - (smaller_len-1)//2])
            elif median1 == median2:
                print 'in 10'
                return median1
            else:
                print 'in 11'
                return self.findMedianSortedArrays(nums2[(smaller_len-1)//2:], nums1[:(len(nums1)) - (smaller_len-1)//2]) 
        #
        if len(nums1) == 0:
            print 'in 1'
            return self.find_median(nums2)
        #
        if len(nums2) == 0:
            print 'in 2'
            return self.find_median(nums1)
        #
        if len(nums1) == 1:
            print 'in 3'
            bisect.insort(nums2, nums1[0])
            return self.find_median(nums2)
        #
        if len(nums2) == 1:
            print 'in 4'
            bisect.insort(nums1, nums2[0])
            return self.find_median(nums1)
        #
        if len(nums1) == 2:
            print 'in 5'
            bisect.insort(nums2, nums1[0])
            bisect.insort(nums2, nums1[1])
            return self.find_median(nums2)
        #
        if len(nums2) == 2:
            print 'in 6'
            bisect.insort(nums1, nums2[0])
            bisect.insort(nums1, nums2[1])
            return self.find_median(nums1)
    #
    def find_median(self,a):
        if len(a) % 2 ==0:
            return (a[len(a)//2]+a[len(a)//2-1]) / 2.0
        else:
            return a[len(a)//2]


# Optimised & Cleaned
import bisect
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        ## General Cases
        if len(nums1) > 2 and len(nums2) > 2:
            print nums1, nums2
            print len(nums1),len(nums2)
            smaller_len = min(len(nums1),len(nums2))
            if nums1[-1] <= nums2[0]:
                return self.find_median(nums1 + nums2)
            if nums2[-1] <= nums1[0]:
                return self.find_median(nums2 + nums1)
            median1 = self.find_median(nums1)
            median2 = self.find_median(nums2)
            if median1 < median2:
                return self.findMedianSortedArrays(nums1[(smaller_len-1)//2:], nums2[:(len(nums2)) - (smaller_len-1)//2])
            elif median1 == median2:
                return median1
            else:
                return self.findMedianSortedArrays(nums2[(smaller_len-1)//2:], nums1[:(len(nums1)) - (smaller_len-1)//2]) 
        ## Base cases
        if len(nums1) == 0:
            return self.find_median(nums2)
        if len(nums2) == 0:
            return self.find_median(nums1)
        if len(nums1) == 1:
            bisect.insort(nums2, nums1[0])
            return self.find_median(nums2)
        if len(nums2) == 1:
            bisect.insort(nums1, nums2[0])
            return self.find_median(nums1)
        if len(nums1) == 2:
            bisect.insort(nums2, nums1[0])
            bisect.insort(nums2, nums1[1])
            return self.find_median(nums2)
        if len(nums2) == 2:
            bisect.insort(nums1, nums2[0])
            bisect.insort(nums1, nums2[1])
            return self.find_median(nums1)
    #
    def find_median(self,a):
        if len(a) % 2 ==0:
            return (a[len(a)//2]+a[len(a)//2-1]) / 2.0
        else:
            return a[len(a)//2]

a = Solution()
a.findMedianSortedArrays([1,2,3],[2,3,4,5,6,7,8,9])


    if (len(nums1)+len(nums2)) % 2 = 0:

    if (len(nums1)+len(nums2)) % 2 = 1:


def a(b):
    if len(b) ==1:
        print 'end'
        return 0
    print '\n\n\n'
    print b, len(b)
    a(b[:len(b)//2])
    return 0


a([1,2,3,4,5,6,7,8])


if 2==1:
    print 'ok'
elif 1==1:
    print 'ok2'
else:
    print 'no'
