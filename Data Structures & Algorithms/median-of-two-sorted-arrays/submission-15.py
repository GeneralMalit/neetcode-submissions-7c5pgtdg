class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        l, r = 0, m

        while l <= r:
            partX = (l + r) // 2
            partY = (m + n + 1) // 2 - partX

            maxLeftX = float("-inf") if partX == 0 else nums1[partX - 1]
            maxLeftY = float("-inf") if partY == 0 else nums2[partY - 1]
            minRightX = float("inf") if partX == m else nums1[partX]
            minRightY = float("inf") if partY == n else nums2[partY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if ((m + n) % 2) == 0:
                    #even
                    return (max(maxLeftX, maxLeftY) +  min(minRightX, minRightY)) / 2

                else:
                    #odd
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                r = partX - 1
            else:
                l = partX + 1
        return -1