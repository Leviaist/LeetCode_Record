class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        mi,m1=0,0
        for i,v in enumerate(mat):
            mi,m1=(i,sum(v)) if sum(v)>m1 else (mi,m1)
        return [mi,m1]