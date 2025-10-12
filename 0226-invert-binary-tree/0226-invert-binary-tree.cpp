// Time Complexity : O(n)
// Space Complexity : O(n)
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        // Base case...
        if(root == NULL){
            return root;
        }
        // Call the function recursively for the left subtree...
        invertTree(root->left);
        // Call the function recursively for the right subtree...
        invertTree(root->right);
        // swapping process...
        TreeNode* curr = root->left;
        root->left = root->right;
        root->right = curr;
        return root;        // Return the root...
    }
};