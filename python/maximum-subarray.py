class Solution:
  # @param A, a list of integers
  # @return an integer
  def maxSubArray(self, A):
    result = A[0]
    f = 0
    for x in A:
      f = max(f+x, x)
      result = max(result, f)
    return result