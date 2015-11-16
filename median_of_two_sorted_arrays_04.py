class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        l = m + n
        if l & 0x01:
            return self.find_kth(nums1, nums2, (l/2)+1)
        else:
            left = self.find_kth(nums1, nums2, l/2)
            right = self.find_kth(nums1, nums2, (l/2)+1)
            mid = (left + right)/2.0
            return mid

    def find_kth(self, nums1, nums2, k):
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.find_kth(nums2, nums1, k)
        if m == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])

        pa = min(k/2, m)
        pb = k - pa
        if nums1[pa-1] < nums2[pb-1]:
            return self.find_kth(nums1[pa:], nums2, k-pa)
        elif nums1[pa-1] > nums2[pb-1]:
            return self.find_kth(nums1, nums2[pb:], k-pb)
        else:
            return nums1[pa-1]
