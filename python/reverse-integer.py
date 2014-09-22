class Solution:
    # @return an integer
    def reverse(self, x):
        isNegative = False
        tempStr = ''
        if (x >= 0):
            tempStr = str(x)
        else:
            isNegative = True
            tempStr = str(-x)
        
        tempStr = tempStr[::-1]
        if (isNegative):
            return (int) ('-' + tempStr)
        return (int) (tempStr)