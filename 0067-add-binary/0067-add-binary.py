class Solution:
  def addBinary(self, a: str, b: str) -> str:

    binary_str1 = a
    binary_str2 = b

    int1 = int(binary_str1, 2)
    int2 = int(binary_str2, 2)

    sum_result = int1 + int2
    binary_sum = bin(sum_result)  
    binary_sum_clean = binary_sum[2:]
    return binary_sum_clean