
# coding: utf-8

# Exploratory Data Analysis
# 
# It is not meant to be a robust financial analysis or be taken as financial advice.
#
# The Imports
# 

# In[30]:


get_ipython().system('pip install pandas-datareader')
get_ipython().system('pip install --upgrade pandas')
import pandas_datareader.data as wb
import datetime
import pandas as pd
import numpy as np
import datetime
get_ipython().magic('matplotlib inline')


# ## Data
# 
# We need to get data using pandas datareader. We will get stock information for the following banks:
# *  Bank of America
# * CitiGroup
# * Goldman Sachs
# * JPMorgan Chase
# * Morgan Stanley
# * Wells Fargo
# 
# # ** Use [this documentation page](https://pandas-datareader.readthedocs.io/en/latest/) for hints and instructions (it should just be a matter of replacing certain values. Use google finance as a source, for example:**
#     
#     # Bank of America
#     BAC = data.DataReader("BAC", 'google', start, end)
# 

# In[39]:

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2017, 1, 1)


# In[36]:

# Bank of America
BAC = wb.DataReader("BAC", 'yahoo', start, end)

# CitiGroup
C = wb.DataReader("C", 'yahoo', start, end)

# Goldman Sachs
GS = wb.DataReader("GS", 'yahoo', start, end)

# JPMorgan Chase
JPM = wb.DataReader("JPM", 'yahoo', start, end)

# Morgan Stanley
MS = wb.DataReader("MS", 'yahoo', start, end)

# Wells Fargo
WFC = wb.DataReader("WFC", 'yahoo', start, end)


# ##### Add a Column_Company Name 

# In[37]:

BAC["Company"]='BOA'
C["Company"]='Citi'
GS["Company"]='GoldmanSachs'
JPM["Company"]='JPMorgan'
MS["Company"]='MorganStanley'
WFC["Company"]='WellsFargo'



# ##### Draw the closing prices of BAC

# In[38]:

import matplotlib.pyplot as plt
BAC.Close.plot(figsize = (15,9),grid = True)


# ##### Append all the data sets

# In[ ]:

# your code here

data = pd.concat([BAC, C, GS, JPM, MS, WFC])
data.head()


# In[ ]:

# create a new dataframe shows stocks' closing prices on each date.
stocks = pd.DataFrame({"BOA": BAC["Close"],
                      "Citi": C["Close"],
                       "GoldmanSachs":GS['Close'],
                       "JPMorgan":JPM['Close'],
                       'MorganStanley':MS['Close'],
                       "WellsFargo":WFC['Close']
                       
                       
                      })
stocks.head()


# ##### Derive the average closing price for each bank

# In[40]:

# your code here
avgcprice=stocks.mean()
print(avgcprice)


# ##### Plot the average closing price for each bank using matplotlib or plotly and cufflinks
# 

# In[41]:

# your code here
avgcprice.plot(kind ="bar",figsize =(15,9))


# 
# ** What is the max Close price for each bank's stock throughout the time period?**

# In[42]:

# your code here
re_max = stocks.max()
print(re_max)


# ** Create a new dataframe called returns. This dataframe will contain the returns for each bank's stock. returns are typically defined by:**
# 
# $$r_t = \frac{p_t - p_{t-1}}{p_{t-1}} = \frac{p_t}{p_{t-1}} - 1$$

# ** We can use pandas pct_change() method on the Close column to create a new dataframe representing this return value. Use .groupby().**

# In[47]:

# 
# drop first row because first trading day has no return value.
# fill the na with 0 in the data 
returns = stocks.pct_change().iloc[1:].fillna(0)

returns



# ** Using this returns DataFrame, figure out on what dates each bank stock had the best and worst single day returns. Did anything significant happen that day?**

# In[44]:


print("Best returns dates:")
print(returns.idxmax())


print("Worst returns date:")
print( returns.idxmin())


# ** Please state here what you have noticed. Did anything significant happen in that time frame? **

# 2016-06-24: U.S. stocks close sharply lower after Britain votes for Brexit.The British people have voted to leave the European Union leaving the market in shock.
# 2016-11-10/2016-11-09 are the best days because of US presidential elections.
# 2016-2/12: Crude has spiked 14% ending  at a 17-month high of $51.68 a barrel on 2nd december
# 

# 

# ** Take a look at the standard deviation of the returns, which stock would you classify as the riskiest over the entire time period? **

# In[45]:

#  your code here
re_std = returns.std()
print(re_std)


# ** Which would you classify as the riskiest for the year 2016? **

# In[46]:

# your code here
print (re_std.max())

print("the riskiest stock is: MorganStanley ")


# ** Create a density plot using any library you like to visualize the previous year's return for each bank **

# ### Moving Averages
# 
# ** Please derive the moving averages for these stocks in the year 2016. Use .rolling() in pandas to get the rolling average calculation. ** 
# 
# 

# In[48]:

# your code here
# your code here
import seaborn as sns  
fig = plt.figure(figsize=(20,10))
sub1 = fig.add_subplot(2,3,1)
sub1=sns.kdeplot(returns['BOA'], shade=True, color="r")
sub1 = fig.add_subplot(2,3,2)
sub1=sns.kdeplot(returns['Citi'], shade=True, color="b")
sub1 = fig.add_subplot(2,3,3)
sub1=sns.kdeplot(returns['GoldmanSachs'], shade=True, color="y")
sub1 = fig.add_subplot(2,3,4)
sub1=sns.kdeplot(returns['JPMorgan'], shade=True, color="g")
sub1 = fig.add_subplot(2,3,5)
sub1=sns.kdeplot(returns['MorganStanley'], shade=True, color="c")
sub1 = fig.add_subplot(2,3,6)
sub1=sns.kdeplot(returns['WellsFargo'], shade=True, color="m")


# In[14]:

# your code here
mov_average = stocks.rolling(window = 30).mean().dropna()

mov_average.head()


# ** Plot the rolling 30 day average against the Close Price for Bank Of America's stock for the year 2016**

# In[32]:


# your code here

boa_mov_avg = mov_average["BOA"]
boa_mov_avg.plot(label='Rolling 30 day average',color = 'blue',figsize = (15,9))
BAC.Close.plot(label='BAC close price',color ='green',figsize = (15,9))
plt.ylabel('Values')
plt.legend(loc='upper left')


# ** Create a heatmap of the correlation between the stocks Close Price.**
# 

# In[27]:

# your code here
# calculate the correlation matrix
import seaborn as sns
corr = stocks.corr()
# plot the heatmap
plt.subplots(figsize=(15,9)) 

sns.heatmap(corr, annot = True, cmap='YlGnBu')
