class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            # Fix first one
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                # fix second one
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left, right = j+1, len(nums)-1
                while left < right:
                    curr_sum = nums[i]+nums[j]+nums[left]+nums[right]
                    if target == curr_sum:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        left += 1 
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif target > curr_sum:
                        left += 1 
                    else:
                        right -= 1

        return res