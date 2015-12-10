class Solution(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sort_nums = sorted(nums)
        l = len(sort_nums)
        left = 0
        right = l - 1
        result = []
        while left < right:
            if sort_nums[left] + sort_nums[right] == target:
                for j in range(l):
                    if nums[j] == sort_nums[left]:
                        result.append(j+1)
                        continue
                    if nums[j] == sort_nums[right]:
                        result.append(j+1)
                    if len(result) == 2:
                        break
                break
            elif sort_nums[left] + sort_nums[right] < target:
                left += 1
            else:
                right -= 1
        return tuple(result)

s = Solution()
a1 = [-1, -2, -3, -4, -5]
r1 = s.two_sum(a1, -8)
a2 = [0, 4, 3, 0]
r2 = s.two_sum(a2, 0)
print r1, r2
