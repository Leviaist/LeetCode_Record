class Solution(object):
    def maximumOr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        high_nums,ret,bit,hb,nmax=[],0,[0],1,max(nums)
        while (hb<<1)<=nmax:
            hb=hb<<1
            bit.append(0)
        for i in nums:
            if i>=hb:
                high_nums.append(i)
            for j in range(len(bit)):
                bit[j]+=i&(1<<j)>=1
        for _ in range(k):
            bit.append(0)
        for i in high_nums:
            sub_bit=[l for l in bit]
            for j in range(len(bit)):
                sub_bit[j]-=i&(1<<j)>=1
            i,weight,sm=i<<k,1,0
            for j in range(len(bit)):
                sub_bit[j]+=i&(1<<j)>=1
            for ii in sub_bit:
                sm,weight=sm+weight*(ii>=1),weight<<1
            ret=max(sm,ret)
        return ret