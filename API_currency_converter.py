#!/usr/bin/env python
# coding: utf-8

# # currency converter
# 

# steps

# gather the parameters of interest

# construct the url and send a get request to it

# for unsuccessful requests print the error message

# for successful requests: extract the relevant data and calculate the result

# display the results to the user

# In[ ]:


date=input("Please enter the date (in the format 'yyyy-mm-dd' or latest)")
base=input("convert from (currency): ")
currency=input("convert to (currency):")
quantity=float(input("how much {} do you want to convert:".format(base)))
import os
from dotenv import load_dotenv
import json
import requests
load_dotenv()
api_key=os.getenv("API_KEY")
url="http://api.exchangeratesapi.io/v1/" +date+ f"?access_key={api_key}"+"&symbols="+currency+"&base="+ base
response=requests.get(url)
if(response.ok is False):
    print("\n Error {}".format(response.status_code))
    print(response.json()["error"])
          
else:
    data=response.json()
    rate=data["rates"][currency]
    result=rate*quantity
    print("\n{0} {1} is equal to {2} {3}, based upon exchange rates on {4}".format(date,base,result,rate,data["date"]))
          
    


# In[15]:


url


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




