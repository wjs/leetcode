class Solution:
  # @return an integer
  def reverse(self, x):
    isNegative = False;
    tempStr = ''
    if x > 0:
      tempStr = str(x)
    else:
      tempStr = str(-x)
      isNegative = True

    tempStr = tempStr[::-1]
    if isNegative:  
      return (int) ('-' + tempStr)
    return (int) (tempStr)