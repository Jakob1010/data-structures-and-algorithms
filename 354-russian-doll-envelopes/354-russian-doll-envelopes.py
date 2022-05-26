class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0],-x[1]))
        
        def LIS(nums):
            sub = []
            for num in nums:
                i = bisect_left(sub,num)
                if i == len(sub):
                    sub.append(num)
                else:
                    sub[i] = num
            return len(sub)
        
        return LIS(list(i[1] for i in envelopes))