#!/usr/bin/env python
# coding: utf-8

# In[28]:


#question 1
ch_1=[2, 3, 6]
m=1
for i in range(len(ch_1)):
    m=ch_1[i]*m
print(m)


# In[37]:


#Question 2
tuple_1=(2:5, 1:2 , 4:4 , 2:3 ,2:1)


# In[21]:


#question 3
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d3 = {}

for i, j in d1.items():

    for x, y in d2.items():

        if i == x:

            d3[i]=(j+y)
        else :
            d3[i]=(j)
            d3[x]=(y)

print(d3)


print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

    


# In[25]:


#question 5
list1= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
for i, j in list1.items():
    list1.sort(j)

    


# In[ ]:




