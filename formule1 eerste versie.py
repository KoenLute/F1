#!/usr/bin/env python
# coding: utf-8

# In[41]:


import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[42]:


st.title("Grand prix info 1950-2022")


# In[43]:


drivers = pd.read_csv("GrandPrix_drivers_details_1950_to_2022.csv")
laps = pd.read_csv("GrandPrix_fastest-laps_details_1950_to_2022.csv", sep =',', encoding='latin-1')
race = pd.read_csv("GrandPrix_races_details_1950_to_2022.csv", sep =',', encoding='latin-1')


# In[44]:


selected_driver = st.sidebar.selectbox('Select a driver', drivers['Driver'].unique())


# In[45]:


driver_laps = laps[laps['Driver'] == selected_driver]
driver_race = race[race['Winner'] == selected_driver]


# In[46]:


points_by_season = drivers.groupby(['year', 'Driver'])['PTS'].sum().reset_index()
driver_points = points_by_season[points_by_season['Driver'] == selected_driver]


# In[47]:


fig, ax = plt.subplots()
ax.plot(driver_points['year'], driver_points['PTS'])
ax.set_xlabel("Season")
ax.set_ylabel("Points")
ax.set_title(f"{selected_driver} Points by Season")


# In[48]:


st.write(f"### {selected_driver}")
st.write("#### Driver Years")
st.write(drivers[drivers['Driver'] == selected_driver])
st.write("#### Fastest Laps")
st.write(driver_laps)
st.write("#### Driver Wins")
st.write(driver_race)
st.pyplot(fig)

