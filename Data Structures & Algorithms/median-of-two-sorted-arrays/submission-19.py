class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        l, r = 0, m

        while l <= r:
            partX = (l + r) // 2
            partY = (m + n + 1) // 2 - partX

            maxL1 = float("-inf") if partX == 0 else nums1[partX - 1]
            maxL2 = float("-inf") if partY == 0 else nums2[partY - 1]
            minR1 = float("inf") if partX == m else nums1[partX]
            minR2 = float("inf") if partY == n else nums2[partY]

            if maxL1 <= minR2 and maxL2 <= minR1:
                if ((m + n) % 2) == 0:
                    return (max(maxL1, maxL2) + min(minR1, minR2)) / 2
                else:
                    return max(maxL1, maxL2)
            elif maxL1 > minR2:
                r = partX - 1
            else:
                l = partX + 1