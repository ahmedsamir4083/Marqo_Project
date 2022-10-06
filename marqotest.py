#!/usr/bin/env python
# coding: utf-8

# In[1]:


conda install marqo


# In[2]:


import marqo

mq = marqo.Client(url='http://localhost:8882')



# In[6]:


mq.index("my-index").add_documents([
    {
        "Title": "leo Messi",
        "Description": "Messi has set the world record for a goals in a single calendar year, with a grand total of 91, beating the previous all-time best set in 1972 by Germany"
    }, 
    {
        "Title": "Cristiano Ronaldo",
        "Description": "Ronaldo's highest season return was 61, which he achieved in 2014-15, and he surpassed the 50-goal mark every season for six years between 2010-11 and 2015-16, ",
    
    },
    {
      "Title": "Mo Salah",
        "Description": "Salah found the back of the net an astonishing 32 times in the 2017/18 season for the Reds."  
    },
    
    {
      "Title": "Andy Cole",
        "Description": "scored 34 goals for Newcastle in 1993/94"  
    },
    
    {
      "Title": "Alan Shearer",
        "Description": "scored 34 goals for Blackburn Rovers in 1994/95 "  
    },
    
    {
      "Title": "Harry Kane",
        "Description": "Kane's breakout season came in 2014-15 when he notched 21 EPL goals "  
    },
     
    {
      "Title": "Thierry Henry",
        "Description": "With 24 goals and 20 assists in the league, Henry set a new record for most assists in a single Premier League season "  
    },
])

results = mq.index("my-index").search(
    q="Who is the best player ever?"
)


# In[7]:


import pprint
pprint.pprint(results)


# In[ ]:




