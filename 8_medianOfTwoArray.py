import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        med = (nums1 + nums2)
        return statistics.median(med)
l1=[1,2]
l2=[3,4]
obj = Solution()
print(obj.findMedianSortedArrays(l1,l2))