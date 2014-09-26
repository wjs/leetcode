class Solution:
  # @param a list of integers
  # @return an integer
  def removeDuplicates(self, A):
    if len(A) == 0: return 0
    index = 0
    for i in xrange(1, len(A)):
      if A[index] != A[i]:
        index += 1
        A[index] = A[i]
    return index+1