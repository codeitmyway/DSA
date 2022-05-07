#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''three function in maxheap
1. Push
2. POP
3. Peak'''


# In[2]:


'''For Push
append element to the last
float it up to its actual position

for POP
Elemenate the first element 
bubble down the new first element 

for Peek
Simply return first element'''


# In[80]:


class Maxheap():
    def __init__(self, items = []):
        self.heap = [0]
        
        for item in items:
            self.heap.append(item)
            
    def push(self, item):
        self.heap.append(item)
        self.__floatup__(len(self.heap)-1)
        return self.heap
        
    def pop(self):
        self.__swap__(1, -1)
        self.heap.pop()
        self.__bubbledown__(1)
        return self.heap
        
    def peek(self):
        return self.heap[1]
    
    def __swap__(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def __floatup__(self, index):
        parent = index//2
        
        if index <= 1:
            return
        
        if index > parent:
            self.__swap__(index, parent)
            self.__floatup__(parent)
            
    def __bubbledown__(self, index):
        
        left = index * 2
        right = (index * 2) + 1
        
        #print(left, right)
        
        target = index
        
        if len(self.heap) > left and self.heap[left] > self.heap[index]:
            target = left
            
        if len(self.heap) > right and self.heap[right] > self.heap[index]:
            target = right
            
        if index != target:
            self.__swap__(index, target)   
            self.__bubbledown__(index)
        


# In[81]:


m = Maxheap([5,2])


# In[82]:


n = [5,2,6]
n[2]


# In[83]:


m.push(6)


# In[84]:


m.pop()


# m.pop()

# In[85]:


m.pop()


# In[ ]:





# In[127]:


import datetime 

time_of_launch = input()
time_of_launch = time_of_launch.replace(' ', ':')
time_of_launch = datetime.datetime.strptime(time_of_launch, '%H:%M')
#time_of_launch = time_of_launch.strftime('%H:%M')

time_taken_to_crash = input()
time_taken_to_crash = time_taken_to_crash.split(' ')
hour = int(time_taken_to_crash[0])
minute = int(time_taken_to_crash[1])
time_change = datetime.timedelta(hours=hour, minutes=minute)

time_to_crash = time_of_launch + time_change

time_to_crash = time_to_crash.strftime('%H:%M')
time_to_crash = time_to_crash.replace(':', ' ')

#time_taken_to_crash = datetime.datetime.strptime(time_taken_to_crash, '%H:%M')
#time_taken_to_crash = time_taken_to_crash.strftime('%H:%M')

#time_to_crash = time_of_launch + time_taken_to_crash


print(time_to_crash)


# In[12]:


test_case = int(input()) ##input testcase

while test_case > 0: #while there are test case
    num_gifts_wanted = int(input()) #input number of gifts
    
    num_gifts_available = int(input()) #input number of gifts available
    
    price_gifts = input() #input price of the given number of gifts
    price_gifts = price_gifts.split(' ')
    
    #Adding each price of gifts into a list
    priceList = []
    priceList = [int(x) for x in price_gifts]
    
    #performed sorting algo to get the price from lowest to highest
    sorted_priceList = sorted(priceList)
    
    #print(sorted_priceList)
    
    #Evaluating the total cost by adding price for the number of gifts required
    cost = 0 
    for i in range(0, num_gifts_wanted):
        cost += int(sorted_priceList[i])
     
    #Printing out the cost
    print(cost)
    
    #Move to next test case
    test_case -= 1
        
    


# In[11]:


time_of_launch


# In[133]:


price_gifts = '20 30'
i = price_gifts.split(' ')
priceList = [i for i in i]
priceList


# In[ ]:




