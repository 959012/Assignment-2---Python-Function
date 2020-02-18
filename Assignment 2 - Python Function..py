#!/usr/bin/env python
# coding: utf-8

# ## Problem Statement

# Q.1 Write a Python Program to implement your own myreduce() function which works exactly like
# Python's built-in function reduce()
# 

# In[10]:


def my_reduce(a, b):
    result = b[0]
    for i in b[1:]:
        result = a(result, i)
    return result


# In[11]:


def do_sum(a1, a2): 
    return a1 + a2
my_reduce(do_sum, [1, 2, 3, 4])


# Q.2 Write a Python program to implement your own myfilter() function which works exactly like
# Python's built-in function filter()

# In[25]:


def my_filter(a,b):
    result=[]
    for i in b :
        if a(i):
            result.append(i)
    return result

def even(item):
    if item%2==0 :
        return True
    else :
        return False


# In[26]:


l=[1,2,3,4,5,9,10]
print(my_filter(even,l))


# Q.3 Implement List comprehensions to produce the following lists. Write List comprehensions to produce the following Lists
#    
#     ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
#    
#     ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# 
#     ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
#     
#     [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
# 
#     [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# 
#     [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[30]:


a = 'ACADGILD'
list = [x for x  in a]
list


# In[42]:


input = ['x','y','z']
result = [x*y for x in input for y in range(1,5)]
result


# In[45]:


input = ['x','y','z']
result = [x*y for y in range(1,5)for x in input]
result


# In[58]:


input = [2,3,4]
result = [[a+b for a in input for b in range(0,3)]]
print(str(result))


# In[60]:


input = [2,3,4,5]
result = [[a+b for a in input] for b in range(0,4)  ]
print(str(result))


# In[62]:


input =[1,2,3]
result = [(b,a) for a in input for b in range(0,4)]
result


# Q.4 Implement a function longestWord() that takes a list of words and returns the longest one.

# In[84]:


def longestWord(word):
    a = []
    for i in word:
        a.append((len(i), i))
    a.sort()
    return a[2]  


# In[86]:


print(longestWord(['Biswa','Sahullll','MLDPAIlllllllllllllllll']))


# Q.5 Write a Python Program(with class concepts) to find the area of the triangle using the below
# formula.
# 
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# 
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.

# In[ ]:





# Q.6 Write a function filter_long_words() that takes a list of words and an integer n and returns the list
# of words that are longer than n.

# In[22]:


def filter_long_words(n, str):
    list = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            list.append(x)
    return list	
print(filter_long_words(2, "what is name"))


# Q.7 Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.
#     
#     Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
#     Here 2,3 and 4 are the lengths of the words in the list.

# In[27]:


a = ['ab','abc','abce']
l = []
for i in a:
    l.append(len(i))
print(l)


# Q.8 Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is
# a vowel, False otherwise.

# In[27]:


def Vowel(char):
    if (char == 'a') or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U':
        return True
    else:
        return False


# ## Great job!
