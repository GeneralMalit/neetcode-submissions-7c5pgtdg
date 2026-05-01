class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums2, nums1 = nums1, nums2
        
        m, n = len(nums1), len(nums2)
        l, r = 0, m

        while l <= r:
            partX = (l + r) // 2
            partY = (m + n + 1) // 2 - partX

            maxLeft1 = float("-inf") if partX == 0 else nums1[partX - 1]
            maxLeft2 = float("-inf") if partY == 0 else nums2[partY - 1]
            minRight1 = float("inf") if partX == m else nums1[partX]
            minRight2 = float("inf") if partY == n else nums2[partY]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                r = partX - 1
            else:
                l = partX + 1
        
            