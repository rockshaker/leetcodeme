class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(l-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = l - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s-target) < abs(result-target):
                    result = s
                if s == target:
                    break
                elif s < target:
                    left += 1
                else:
                    right -= 1
        return result
