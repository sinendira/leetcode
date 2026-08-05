class Solution(object):
    def nextPermutation(self, nums):
        n=len(nums)
       
        if nums==sorted(nums,reverse=True): #base case
            nums[:]=sorted(nums)
            return nums
        
        for i in range(n-1,0,-1): #finding the dip index from back
            if nums[i]>nums[i-1]:
                index=i-1
                break
        
        for j in range(n-1,index,-1): #swapping to form the just greater number
            if nums[j]>nums[index]:
                temp=nums[j]
                nums[j]=nums[index]
                nums[index]=temp
                break

        (nums[index+1:])=(nums[index+1:][::-1]) # reversing the remaing part
        return nums