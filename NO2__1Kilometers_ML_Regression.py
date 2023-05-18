#!/usr/bin/env python
# coding: utf-8

# In[103]:


import pandas as pd
import dtale
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout
from sklearn.metrics import mean_squared_error, mean_absolute_error,explained_variance_score
import glob
import dask.dataframe as dd
import xarray as xr
from scipy import stats
from sklearn.svm import SVR
from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor


# In[104]:


#Calculation for May 2018

df_May_2018= pd.read_csv('2018 May Grnd.csv')
df=df_May_2018

MEAN_NO2_may=df['MEAN_NO2'].values
NO2_satellite_may=df['NO2_satellite'].values

df['NO2_satellite_box'],_ = stats.boxcox(df['NO2_satellite'])
colors = np.where(df.COUNT > 300, 'r', 'b')
df.plot.scatter(x='MEAN_NO2',y='NO2_satellite_box', c=colors)
df.plot.scatter(x='MEAN_NO2',y='NO2_satellite', c=colors)

scaler=MinMaxScaler()
MEAN_NO2=df['MEAN_NO2'].values
MEAN_NO2=MEAN_NO2.reshape(-1,1)
MEAN_NO2=scaler.fit_transform(MEAN_NO2)


NO2_satellite=df['NO2_satellite'].values
NO2_satellite=NO2_satellite.reshape(-1,1)
NO2_satellite=scaler.fit_transform(NO2_satellite)



df['MEAN_NO2_T']= pd.DataFrame(MEAN_NO2)
df['NO2_satellite_T']= pd.DataFrame(NO2_satellite)

#df.corr()['MEAN_NO2_T'].sort_values().plot(kind='bar')

fig = plt.figure(figsize=(14,6))
plt.plot(MEAN_NO2,marker="o", ms = 10, mfc = 'r', linestyle='None',label='Ground Station')
plt.plot(NO2_satellite,marker="v", ms = 10,linestyle='None', mfc = 'w',label='Satellite')
plt.title('Correlation between Ground and Satellite for May 2018')
plt.legend(loc='best',prop={'size':14})
plt.xlabel('Ground Station')
plt.ylabel('Satellite')



corr=df.corr()['MEAN_NO2'].sort_values()

corr=list(corr)

grnd_corr_may=corr[2]


# In[105]:


#Reading CAMs Data for May 2018
no2_may = xr.open_dataset("CAMS_2018_May_12.00_Surface.nc", engine="netcdf4")
no2_may


# In[106]:


#Extracting Each Variables 
tno2_may=no2_may.tcno2
u10_may=no2_may.u10
v10_may=no2_may.v10
t2m_may=no2_may.t2m
lsp_may=no2_may.lsp


# In[107]:


u10_may.data.shape


# In[108]:


#Finding the index for particular Lat and Lon
lat_ind= np.where(tno2_may.latitude.data==38) 
lon_ind= np.where(tno2_may.longitude.data==122)
lat_ind=int(lat_ind[0])
lon_ind=int(lon_ind[0])
print(no2_may.longitude.data[lon_ind:lon_ind+14])
print(tno2_may.latitude.data[lat_ind:lat_ind+14])


# In[109]:


#Extracting No2 for the bay area for The Month of May
cams_no2=[]
for i in range(31):
   cams_no2_1=list(tno2_may.data[i,lon_ind:lon_ind+14,0])
   cams_no2_2=list(tno2_may.data[i,0,lat_ind:lat_ind+14])
   cams_no2=cams_no2+cams_no2_1+cams_no2_2
   #print(cams_no2)


# In[110]:


#Extracting u10 (10 metre U wind component) for the bay area for The Month of May
cams_u10=[]
for i in range(31):
   cams_u10_1=list(u10_may.data[i,lon_ind:lon_ind+14,0])
   cams_u10_2=list(u10_may.data[i,0,lat_ind:lat_ind+14])
   cams_u10=cams_u10+cams_u10_1+cams_u10_2


# In[111]:


#Extracting v10 (10 metre V wind component) for the bay area for The Month of May
cams_v10=[]
for i in range(31):
   cams_v10_1=list(v10_may.data[i,lon_ind:lon_ind+14,0])
   cams_v10_2=list(v10_may.data[i,0,lat_ind:lat_ind+14])
   cams_v10=cams_v10+cams_v10_1+cams_v10_2


# In[112]:


#Extracting t2m (2 metre temperature) for the bay area for The Month of May
cams_t2m=[]
for i in range(31):
   cams_t2m_1=list(t2m_may.data[i,lon_ind:lon_ind+14,0])
   cams_t2m_2=list(t2m_may.data[i,0,lat_ind:lat_ind+14])
   cams_t2m=cams_t2m+cams_t2m_1+cams_t2m_2


# In[113]:


#Extracting lsp (Large-scale precipitation) for the bay area for The Month of May
cams_lsp=[]
for i in range(31):
   cams_lsp_1=list(lsp_may.data[i,lon_ind:lon_ind+14,0])
   cams_lsp_2=list(lsp_may.data[i,0,lat_ind:lat_ind+14])
   cams_lsp=cams_lsp+cams_lsp_1+cams_lsp_2


# In[114]:


df['cams_u10']=cams_no2
df['cams_u10']=cams_u10
df['cams_v10']=cams_v10
df['cams_t2m']=cams_t2m
df['cams_t2m']=cams_lsp


# In[115]:


df=df.drop(['COUNT','NO2_satellite','NO2_satellite_box'],axis=1)


# In[116]:


dtale.show(df)


# In[117]:


X=df.drop('MEAN_NO2',axis=1).values
y=df['MEAN_NO2'].values


# In[118]:


clf = GridSearchCV(SVR(gamma='auto'), {
    'C': [20,50,100],
    'kernel': ['rbf','linear']
}, cv=5, return_train_score=False)
clf.fit(X,y)


# In[119]:


clf.best_params_


# In[120]:



clf.best_score_


# In[121]:


model_params = {
    'svm': {
        'model': SVR(gamma='auto'),
        'params' : {
            'C': [1,10,20],
            'kernel': ['rbf','linear']
        }  
    },
    'random_forest': {
        'model': RandomForestRegressor(),
        'params' : {
            'n_estimators': [1,5,10]
        }
    },
}


# In[131]:


scores = []

for model_name, mp in model_params.items():
    clf =  GridSearchCV(mp['model'], mp['params'], cv=5, return_train_score=False)
    clf.fit(X, y)
    scores.append({
        'model': model_name,
        'best_score': clf.best_score_,
        'best_params': clf.best_params_
    })
    
df_score = pd.DataFrame(scores,columns=['model','best_score','best_params'])
df_score


# In[123]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)


# In[124]:


model = SVR(kernel='linear', C=20, gamma='auto', degree=2, epsilon=.1,
               coef0=1)
model.fit(X_train,y_train)


# In[125]:


prediction=model.predict(X_test)
MSE=mean_squared_error(y_test,prediction)
print("Mean Squared Error =",MSE)


# In[126]:


RMSE=mean_squared_error(y_test,prediction, squared=False)
print("Root Mean Square Error =",RMSE)


# In[127]:


plt.figure(figsize=(12,6))
plt.scatter(y_test,prediction)
plt.plot(y_test,y_test,'r')
plt.title('Actual vs Predicted No2 (mol/m2) on Test Data')
plt.xlabel('Actual  No2 (mol/m2)')
plt.ylabel('Predicted  No2 (mol/m2)')


# In[128]:


all_prediction=model.predict(X)


# In[129]:


Mean_no2=df['MEAN_NO2']


# In[ ]:


plt.figure(figsize=(12,6))
plt.scatter(Mean_no2,all_prediction)
plt.plot(Mean_no2,Mean_no2,'r')
plt.title('Actual vs Predicted No2 (mol/m2) on Whole Data')
plt.xlabel('Actual  No2 (mol/m2)')
plt.ylabel('Predicted  No2 (mol/m2)')


# In[ ]:


df_June_2018= pd.read_csv('2018 June Grnd.csv')
df_June_2018


# In[ ]:


X_un=df_June_2018.drop('MEAN_NO2',axis=1).values
y_un=df_June_2018['MEAN_NO2'].values


# In[ ]:


prediction=model.predict(X_un)
MSE=mean_squared_error(y_un,prediction)
print("Mean Squared Error on Unseen Data=",MSE)


# In[ ]:


RMSE=mean_squared_error(y_un,prediction, squared=False)
print("Root Mean Square Error on Unseen Data=",RMSE)

