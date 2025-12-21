class Solution(object):
    def containsDuplicate(self, nums):
        historic=set()
        for num in nums :
            if num in historic :
                return True 
            else : 
                historic.add(num)
        return False 
        
