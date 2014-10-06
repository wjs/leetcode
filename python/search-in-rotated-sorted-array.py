class Solution:
  # @param A, a list of integers
  # @param target, an integer to be searched
  # @return an integer
  def search(self, A, target):
    first = 0
    last = len(A)
    while first != last:
      mid = (first + last) / 2
      if (A[mid] == target):
        return mid
      if A[first] <= A[mid]:
        if A[first] <= target and target < A[mid]:
          last = mid
        else:
          first = mid + 1
      else:
        if A[mid] < target and target <= A[last-1]:
          first = mid + 1
        else:
          last = mid
    return -1