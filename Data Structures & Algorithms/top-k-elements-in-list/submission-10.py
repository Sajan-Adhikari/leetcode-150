class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        
        res = [[] for item in count.items()]
        res.append([])

        for key,value in count.items():
            res[value].append(key)

        output=[]
        for i in range(len(res)-1,-1,-1):
            
            for i in range((len(res[i]))-1,-1,-1):
                if len(output)==k:
                    return output
                output.append(res[i])

            


