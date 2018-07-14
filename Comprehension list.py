
# coding: utf-8

# In[29]:


A_letters = []

for letter in 'ACADGILD':
    A_letters.append(letter)

print(A_letters)


# In[31]:


input_list = ['x','y','z']
result = [ item*num for item in input_list for num in range(1,5)  ]
print(str(result))


# In[32]:


input_list = ['x','y','z']
result = [ item*num for num in range(1,5) for item in input_list  ]
print(str(result))


# In[33]:


input_list = [2,3,4]
result = [ [item+num] for item in input_list for num in range(0,3)]
print(str(result))


# In[34]:


input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)  ]
print(str(result))


# In[35]:


input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print(str(result))

