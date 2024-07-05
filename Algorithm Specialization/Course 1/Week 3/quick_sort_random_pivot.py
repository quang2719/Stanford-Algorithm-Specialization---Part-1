class Solution:
    def quick_sort(self, nums):
        if len(nums) <= 1: return nums
        pivot = nums[0]
        new_nums = [0] * len(nums)
        l,r = 0, (len(nums) -1)
        for x in nums:
            if(x<pivot):
                new_nums[l] = x
                l+=1
            elif x >pivot:
                new_nums[r] = x
                r-=1
        new_nums[l] = pivot
        return (
            self.quick_sort(new_nums[:l]) + [pivot] + 
            self.quick_sort(new_nums[l+1:])
        )
    
                
        
    def sortArray(self, nums: List[int]) -> List[int]:
        nums = self.quick_sort(nums)
        return nums