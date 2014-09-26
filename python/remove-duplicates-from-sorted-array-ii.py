class Solution:
  # @param a list of integers
  # @return an integer
  def removeDuplicates(self, A):
    if len(A) <= 2: return len(A)
    index = 2
    for i in xrange(2, len(A)):
      if A[index-2] != A[i]:
        A[index] = A[i]
        index += 1
    return index