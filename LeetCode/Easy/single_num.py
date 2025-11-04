# def singleNumber(self, nums: List[int]) -> int:
#     count = {}
#     for num in nums:
#       if num in count:
#         count[num] += 1
#       else:
#         count[num] = 1
#     for num, freq in count.items():
#       if freq == 1:
#         return num

def singleNumber(self, nums: List[int]) -> int:
    result = 0
    for num in nums:
      result ^= num
    return result