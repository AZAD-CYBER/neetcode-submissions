class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for n in nums:
            dic[n] = dic.get(n, 0) + 1

        sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        ans = []
        for key, val in sorted_dic:
            ans.append(key)
            if len(ans) == k:
                break

        return ans