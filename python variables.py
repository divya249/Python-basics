#!/usr/bin/env python
# coding: utf-8

# # python libraries

# In[2]:


#list
#set
#dictionary
#tuple


# # list

# In[3]:


a=[10,20,30]


# In[4]:


print(type(a))


# In[5]:


#allowes duplictaes

a=[10,10,20,20,30,30]


# In[6]:


print(a)


# In[7]:


a.append(40)


# In[9]:


print(a)


# In[11]:


# modify values
a[3]=50


# In[12]:


print(a)


# In[13]:


# remove values 
a.pop(3)


# In[14]:


print(a)


# In[15]:


a[4]=40


# In[16]:


print(a)


# In[17]:


a.pop(0)


# In[18]:


print(a)


# In[25]:


a[0]=10


# In[26]:


a[3]=40


# In[27]:


print(a)


# In[28]:


# insert values
a.insert(4,50)


# In[29]:


print(a)


# In[30]:


print(a[2])


# # NOTE
#      Lists are used to store Multiple items in a single variable.Lists items are changable,ordered,and allow duplicate values.
#      Lists are indexed,the first item has index[0],the second item has index [1] etc.
#         lists are created using square brackets
#      

# # set

# In[33]:


A={10,20,30,40,50}


# In[34]:


print(type(A))


# In[35]:


A.add(60)


# In[36]:


#unordered
print(A)


# In[37]:


A.remove(20)


# In[38]:


#unindexed
print(A)


# In[39]:


A.discard(10)


# In[40]:


print(A)


# In[41]:


A.pop()


# In[42]:


print(A)


# # NOTE:
#       sets are used to store multiple items in a single variable.
#       A set is a collection which is unordered,unchangable and unindexed.
#      *sets are written with curly brackets,
#      *sets are unordered so we cannot be sure in which order the items will appear
#      *duplicates not allowed

# # tuple

# In[44]:


B=("APPLE",1,"TRUE")


# In[46]:


print(type(B))


# In[47]:


# Allow duplicates

B=("apple","APPLE",1,1,"true","true")


# In[48]:


print(B)


# In[49]:


print(len(B))


# # NOTE:
#      tupels are used to store multiple items in a single variable.
#      *tuples are written with round brackets,
#      *tuple items are ordered,unchangable,and allow duplicate values.

# # Dictionary

# In[50]:


dic={"A":10,"B":20,"C":30}


# In[51]:


print(type(dic))


# In[55]:


print(dic["B"])


# In[56]:


#ordered
print(dic)


# In[59]:


#changable
dic.pop("B")


# In[60]:


print(dict)


# In[61]:


dict.update({"d":40})


# In[62]:


dict


# # NOTE:
#       dictionaries are used to store data values in key:value pairs
#       *dictionary items are ordered,changable,and does  not allow duplicate values
#       * we can add or delete values after the dictionary has been created
#       *dictionary cannot have two items with the same key:pairs
#      

# In[ ]:




