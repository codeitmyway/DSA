#!/usr/bin/env python
# coding: utf-8

# In[11]:


'biraj' < 'hemant'


# In[136]:


'''Create simple binary tree'''

class binary_tree():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# In[14]:


node0 = binary_tree(3)
node1 = binary_tree(4)
node2 = binary_tree(5)


# In[15]:


node0


# In[16]:


node0.key


# In[17]:


node0.left = node1
node0.right = node2


# In[18]:


tree = node0


# In[20]:


tree.key


# In[22]:


tree.left.key


# In[23]:


tree.right.key


# In[1]:


'''Example 2'''
class tree_structure():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# In[4]:


'''node0 = tree_structure(2)
node1 = tree_structure(3)
node2 = tree_structure(5)
node3 = tree_structure(1)
node4 = tree_structure(3)
node5 = tree_structure(7)
node6 = tree_structure(4)
node7 = tree_structure(6)
node8 = tree_structure(8)'''
'''Create Tree from a tuple'''
def parse_tuple(data):
    print(data)
    
    if isinstance(data, tuple) and len(data)==3:
        node = tree_structure(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data == None:
        node = None
    else:
        node = tree_structure(data)
        
    return node


# In[5]:


node0.key


# In[34]:


data = ((1,3,None), 2, ((None, 3, 4),5,(6,7,8)))
tree = parse_tuple(data)


# In[35]:


if tree.left.right:
    print('hi')
else:
    print('yello')


# In[54]:


tree.left.right.key


# In[69]:


'''create tuple from a tree'''

'''Get the tree
1Assign key to c
2assign left key to l
3assign right key to r
4assign center to c

repeat 3 and 4 by using recursion if there are more nodes to be added in left and right nodes'''

def tree_to_tuple(tree):
    
    '''if tree.left == False and tree.right == True:
        c = tree.key
        l = None
        r = tree_to_tuple(tree.right)
    elif tree.right == False and tree.left == True:
        c = tree.key
        l = tree_to_tuple(tree.left)
        r = None
    else:'''
    #if tree.left != None and tree.right != None:
    
    '''if isinstance(tree, tree_structure):
        return(
            tree.key,
            tree_to_tuple(tree.left.key),
            tree_to_tuple(tree.right.key)
        )
    else:
        return tree'''
    
    if isinstance(tree, tree_structure):

        #  special case if the tree has no left and no right sub-tree
        
        if tree.left is not None and tree.right is not None:
            return (
            #print(tree.key)
            tree_to_tuple(tree.left),
            tree.key,
            tree_to_tuple(tree.right)
            )
        if tree.left is None and tree.right is not None:
            #print(tree.key)
            return (
                #print(tree.key)
                None,
                tree.key,
                tree_to_tuple(tree.right)
            )
        elif tree.left is not None and tree.right is None:
            return (
                #print(tree.key)
                tree_to_tuple(tree.left),
                tree.key,
                None
            )
            

        '''return (
            #print(tree.key)
            tree_to_tuple(tree.left),
            tree.key,
            tree_to_tuple(tree.right)
        )'''
    #raise ValueError('this is not a tree')

    '''if l == None and r != None:
        c = tree.key
        l = None
        r = tree_to_tuple(tree.right)
    elif r == None and l != None:
        c = tree.key
        l = tree_to_tuple(tree.left)
        r = None'''


# In[70]:


tree_to_tuple(tree)


# In[25]:


t


# In[39]:


'''if node.left & node.right = none
than display node.key

else
call recursion and pass left and right node again
'''

def display_key(tree, space='\t', level=0):
    
    #if node is empty
    if tree is None:
        print(space*level + '*')
        return
    
    #if node is a leaf
    if tree.left is None and tree.right is None:
        print(space*level + str(tree.key))
        return
    
    #if the node has children
    display_key(tree.right, space, level+1)
    print(space*level + str(tree.key))
    display_key(tree.left, space, level+1)
    
    
    
        
    
    


# In[40]:


display_key(tree)


# In[78]:


#Inorder traversal
def tree_traversal(tree):
    if tree is None:
        return []
    
    return( tree_traversal(tree.left) + 
              [tree.key] +
              tree_traversal(tree.right))


# In[79]:


tree_traversal(tree)


# In[81]:


tree.left.key


# In[82]:


#Preorder traversal
def preorder_traversal(tree):
    
    if tree is None:
        return []
    
    return(
        [tree.key] +
        preorder_traversal(tree.left) +
        preorder_traversal(tree.right)
    )


# In[83]:


preorder_traversal(tree)


# In[84]:


#postorder traversal
def postorder_traversal(tree):
    
    if tree is None:
        return[]
    
    return(
        postorder_traversal(tree.left)+
        postorder_traversal(tree.right)+
        [tree.key]
    )


# In[85]:


postorder_traversal(tree)


# In[86]:


max(tree.left)


# In[ ]:




