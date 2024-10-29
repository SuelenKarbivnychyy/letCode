class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numbers = {}

        for num in nums:
            if num in numbers.keys():
                numbers[num]+=1
            else:
                numbers[num]=1

        for key, value in numbers.items():
            if value == 1:
                return key  
       

task = Solution()
task.singleNumber([2,2,1])                
        