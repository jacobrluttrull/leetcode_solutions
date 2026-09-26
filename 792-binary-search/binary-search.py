class Solution:
    def search(self, nums: list[int], target: int) -> int:
        length = len(nums)
        beg = 0
        end = length - 1
        while beg <= end:
            mid = (beg + end) // 2
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                beg = mid + 1
            else:
                end = mid - 1
        return -1
