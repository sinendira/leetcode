class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            temp_list = []

            for subset in res:
                new_subset = subset + [num]

                temp_list.append(new_subset)

            res += temp_list    

        return res        