class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l = len(nums)
        if l < 4:
            return []

        nums.sort()
        result = []
        for i in range(l-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, l-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = l - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left-1] == nums[left]:
                            left += 1
                        while left < right and nums[right+1] == nums[right]:
                            right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return result
