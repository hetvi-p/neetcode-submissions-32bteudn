class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        freq = [[] for i in range(len(nums) + 1)]
            
        for n in count.keys():
            freq[count[n]].append(n)
        
        res = []
        print(freq)

        for n in freq[::-1]:
            print(len(n) + len(res))
            if n and len(n) + len(res) <= k:
                print(res + n)
                res = res + n

        return res


        #[(), (0, 2) (12), (13)]
        
        


        

            




                                 
        