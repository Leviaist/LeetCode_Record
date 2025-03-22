class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for i,j in enumerate(nums):
            hashmap[j]=i
        for i,j in enumerate(nums):
            if target-j in hashmap:
                if i==hashmap[target-j]:
                    continue
                return [i,hashmap[target-j]]