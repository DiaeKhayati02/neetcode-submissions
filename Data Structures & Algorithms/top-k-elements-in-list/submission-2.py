class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = 0 
        dict2 = {}
        dict2 = {}
        for n in nums:
            if n in dict2:
                dict2[n] += 1
            else:
                dict2[n] = 1
        
    

        sorted_dict = dict(sorted(dict2.items(), key=lambda x: x[1], reverse=True))
        keys = list(sorted_dict.keys())
        final=[]
        for i in range(k):
            final.append(keys[i])

        return final
            
            
