/*
    作业1:构建一棵二叉树，实现二叉树的前中后序遍历
*/

#include "std.h"
// Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

//递归实现遍历
class Solution
{
public:
    vector<int> result;
    
    // 力扣144. 二叉树的前序遍历
    vector<int> preorderTraversal(TreeNode *root)
    {
        preTraversal(root);
        return result;
    }
    void preTraversal(TreeNode *root)
    {
        if (!root)
            return;
        result.push_back(root->val);
        preTraversal(root->left);
        preTraversal(root->right);
    }

    // 94. 二叉树的中序遍历
    vector<int> inorderTraversal(TreeNode *root)
    {
        inTraversal(root);
        return result;
    }
    void inTraversal(TreeNode *root)
    {
        if (!root)
            return;
        inTraversal(root->left);
        result.push_back(root->val);
        inTraversal(root->right);
    }

    // 145. 二叉树的后序遍历
    vector<int> postorderTraversal(TreeNode *root)
    {
        postTraversal(root);
        return result;
    }
    void postTraversal(TreeNode *root)
    {
        if (!root)
            return;
        postTraversal(root->left);
        postTraversal(root->right);
        result.push_back(root->val);
    }
};

//非递归实现遍历(用栈模拟)
class Solution2
{
public:

    // 力扣144. 二叉树的前序遍历
    vector<int> preorderTraversal(TreeNode *root)
    {
        vector<int> result;
        stack<TreeNode *> st;
        st.push(root);
        while (!st.empty())
        {
            auto top = st.top();
            st.pop();
            if (!top)
                continue;
            result.push_back(top->val);
            st.push(top->right);
            st.push(top->left);
        }
        return result;
    }

    // 94. 二叉树的中序遍历
    vector<int> inorderTraversal(TreeNode *root)
    {
        vector<int> result;
        stack<TreeNode *> st;
        TreeNode *cur = root;
        while (cur || !st.empty())
        {
            while (cur)
            {
                st.push(cur);
                cur = cur->left;
            }
            cur = st.top();
            st.pop();
            result.push_back(cur->val);
            cur = cur->right;
        }
        return result;
    }

    // 145. 二叉树的后序遍历
    vector<int> postorderTraversal(TreeNode *root)
    {
        vector<int> result;
        stack<TreeNode *> st;
        st.push(root);
        while (!st.empty())
        {
            auto top = st.top();
            st.pop();
            if (!top)
                continue;
            result.push_back(top->val);
            st.push(top->left);
            st.push(top->right);
        }
        reverse(result.begin(), result.end());
        return result;
    }
};