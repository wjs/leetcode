# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if (root == None): 
            return 0
      arr = [root]
      return self.BFSCount(arr, 1)

    def BFSCount(self, nodeArr, depth):
      tempArr = []
      for node in nodeArr:
          if (node != None):
            if (node.left): tempArr.append(node.left)
            if (node.right): tempArr.append(node.right)
      if (len(tempArr) > 0): 
        depth = depth + 1
        return self.BFSCount(tempArr, depth)
      else:
        return depth