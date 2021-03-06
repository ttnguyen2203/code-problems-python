'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that 
adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Difficulty: Easy - Medium

Solution notes:
O(n) time
O(1) space
'''

def path_sum (root, k):
	if root == null or k < 0:
		return False
	if root.left == null and root.right == null:
		return k == root.val
	else:
		return path_sum(root.left, k-root.val) or path_sum(root.right, k-root.val)

