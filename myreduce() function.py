
# coding: utf-8

# In[4]:


def myreduce(function, sequence):
    tally = sequence[0]
    for next in sequence[1:]:
        tally = function(tally, next)
    return tally
myreduce((lambda x,y: x+y), [1,2,3,4,5])


# In[5]:


from functools import reduce
reduce((lambda x,y: x+y), [1,2,3,4,5])

