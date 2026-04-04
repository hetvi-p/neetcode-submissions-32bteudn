class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        r = []
        for n in nums:
            if count.get(n):
                count[n] += 1
            else:
                count[n] = 1

        val = list(count.values())
        val.sort()
        print(val)
        val = val[-k:]

        for n in val:
            for k, v in count.items():
                if n == v and k not in r:
                    r.append(k)
            

        return r



            
        