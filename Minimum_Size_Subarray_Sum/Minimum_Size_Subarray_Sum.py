class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        minlen=float('inf')
        l=0

        for r in range(len(nums)):
            sum+=nums[r]

            while sum>=target :
                curlen=r-l+1
                minlen=min(minlen,curlen)
                sum-=nums[l]
                l+=1
        
        if minlen==float('inf'):
            return 0
        else :
            return minlen
        
