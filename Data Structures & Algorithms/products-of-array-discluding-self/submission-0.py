class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        premul=[1]*n
        postmul=[1]*n
        pre=1
        post=1
        for i in range(n):
            pre*=nums[i]
            premul[i]=pre
            post*=nums[n-1-i]
            postmul[n-1-i]=post
        res=[postmul[1]]
        for i in range(1,n-1):
            res.append(premul[i-1]*postmul[i+1])
        res.append(premul[n-2])
        return res
            