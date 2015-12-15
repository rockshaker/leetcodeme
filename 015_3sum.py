class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        if l < 3:
            return []

        nums.sort()
        result = []
        check_nums = []
        for i in range(l):
            if nums[i] not in check_nums:
                check_nums.append(nums[i])
            else:
                continue
            remain_nums = [nums[j] for j in range(i+1, l)]
            left = 0
            right = len(remain_nums) - 1
            while left < right:
                if nums[i] + remain_nums[left] + remain_nums[right] > 0:
                    right -= 1
                elif nums[i] + remain_nums[left] + remain_nums[right] < 0:
                    left += 1
                else:
                    tmp = [nums[i], remain_nums[left], remain_nums[right]]
                    result.append(tmp)

                    left += 1
                    right -= 1

                    while left < right and remain_nums[left] == remain_nums[left-1]:
                            left += 1
                    while left < right and remain_nums[right] == remain_nums[right+1]:
                            right -= 1
            i += 1
        return result

s = Solution()
print s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
