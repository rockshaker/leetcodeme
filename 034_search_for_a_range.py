class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        if right == 0:
            if nums[right] == target:
                return [0, 0]
            else:
                return [-1, -1]

        result = []
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                result.append(mid)
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if result:
            i = result[0] - 1
            j = result[0] + 1
            prev_flag = 0
            post_flag = 0
            if i >= 0:
                while nums[i] == target:
                    prev_flag += 1
                    i -= 1
                    if i < 0:
                        break
            if j <= len(nums)-1:
                while nums[j] == target:
                    post_flag += 1
                    j += 1
                    if j > len(nums)-1:
                        break
            prev = result[0] - prev_flag
            post = result[0] + post_flag
            result = [prev, post]
        else:
            result = [-1, -1]

        return result
