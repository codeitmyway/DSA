#!/usr/bin/env python
# coding: utf-8

# In[2]:


nums = [-1,0,3,5,9,12]
target = 2

lo = 0
hi = len(nums)-1


while lo <= hi:

    mid = (lo + hi) // 2
    print('lo' ,lo, 'Mid' ,  mid, 'hi' , hi)
    if nums[mid] == target:
        try:
            print(mid)
        except:
            print(-1)
        break
    elif nums[mid] > target:
        hi = mid -1
    elif nums[mid] < target:
        lo = mid + 1
        
    print(-1)


# In[ ]:


n = 10

lo = 0
hi = n-1


while lo <= hi:

    mid = (lo + hi) // 2
    num = guess(mid)
    #print('lo' ,lo, 'Mid' ,  mid, 'hi' , hi)
    if num == 0:
        try:
            return(n[mid])
        except:
            return(-1)
        break
    elif num == -1:
        hi = mid -1
    elif num == 1:
        lo = mid + 1

    return(-1)


# In[22]:


'''Find the number of rotations from given rotated sorted array'''

def count_rotation(nums):
    low_num = min(nums)
    '''index_of_ln = nums.index(low_num)
    return(index_of_ln)'''
    
    lo = 0
    hi = len(nums)-1
    
    while lo < hi:
        mid = (lo+hi) //2
        
        if low_num == nums[mid]:
            return(mid)
        
        elif nums[mid] > nums[hi]:
            lo = mid + 1
            
        elif nums[mid] < nums[hi]:
            hi = mid - 1
            
        
    return(-1)
        
            



# In[28]:


test = {
    'input' : { 'nums' : [3,4,5,1,2]},
    'output' : 3
}


# In[29]:


nums = test['input']['nums']
output = test['output']

ac_output = count_rotation(nums)

output == ac_output


# In[30]:




# In[ ]:




