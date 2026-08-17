class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dico = {}
        for i, j in enumerate(nums):
            dico[i] = j
        for k_idx, k in dico.items():
            for v_idx, v in dico.items():
                if k_idx != v_idx and k + v == target:
                    return [k_idx, v_idx]