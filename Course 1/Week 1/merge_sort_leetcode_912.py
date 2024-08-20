class Solution:
    def merge_2_arr(self,arr1,arr2): 
        if len(arr1) == 0 or len(arr2) ==0:
            return arr1+arr2
        arr3 = []
        i,j = 0,0
        while(i <len(arr1) and j < len(arr2)):
            if(arr1[i] < arr2[j]):
                arr3.append(arr1[i])
                i+=1
            else:
                arr3.append(arr2[j])
                j+=1
        while i < len(arr1): 
            arr3.append(arr1[i])
            i+=1
        while j < len(arr2):
            arr3.append(arr2[j])
            j+=1
        return arr3
    
    def merge_sort(self,arr):
        if len(arr)==1:
            return arr
        mid = len(arr)//2
        l_arr = arr[:mid]
        r_arr = arr[mid:]
        l_arr = self.merge_sort(l_arr)
        r_arr = self.merge_sort(r_arr)
        arr = self.merge_2_arr(l_arr,r_arr)
        return arr
                
        
    def sortArray(self, nums: List[int]) -> List[int]:
        nums = self.merge_sort(nums)
        return nums