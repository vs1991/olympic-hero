# --------------
import pandas as pd 
#loading data
data=pd.read_csv(path)
print(data)

#renaming columns 
data.rename(columns={'Total':'Total_Medals'},inplace=True)
print(data)

#display first 10 records
data.head(11)


# --------------
#Code starts here
import numpy as np




data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],'Both',data['Better_Event'])
#print(data)
#print(data['Better_Event'])
better_event=data['Better_Event'].value_counts().index.values[0]
print(better_event)


# --------------
#Code starts here
import pandas as pd 


top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries=top_countries[:-1]


def top_ten(data,col):
    country_list=[]
    country_list=list((data.nlargest(10,col)['Country_Name']))
    return country_list

top_10_summer=top_ten(top_countries,'Total_Summer')
print(top_10_summer)

top_10_winter=top_ten(top_countries,'Total_Winter')
print(top_10_winter)

top_10=top_ten(top_countries,'Total_Medals')
print(top_10)


common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)



# --------------
#Code starts here
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

summer_df=data[data['Country_Name'].isin(top_10_summer)]
print(summer_df)

winter_df=data[data['Country_Name'].isin(top_10_winter)]
print(winter_df)

top_df=data[data['Country_Name'].isin(top_10)]
print(top_df)

summer_df.plot.bar(x='Country_Name',y='Total_Summer')

winter_df.plot.bar(x='Country_Name',y='Total_Winter')

top_df.plot.bar(x='Country_Name',y='Total_Medals')


# --------------
#Code starts here

summer_df['Golden_Ratio']=data['Gold_Summer']/data['Total_Summer']
summer_max_ratio=max(summer_df['Golden_Ratio'])
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_country_gold)

winter_df['Golden_Ratio']=data['Gold_Winter']/data['Total_Winter']
winter_max_ratio=max(winter_df['Golden_Ratio'])
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
print(winter_country_gold)

top_df['Golden_Ratio']=data['Gold_Total']/data['Total_Medals']
top_max_ratio=max(top_df['Golden_Ratio'])
top_country_gold=summer_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print(top_country_gold)


# --------------
#Code starts here
data_1=data[:-1]




data_1['Total_Points']=data_1['Gold_Total']*3 + data_1['Silver_Total']*2+data_1['Bronze_Total']*1

most_points=max(data_1['Total_Points'])

best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']



# --------------
#Code starts here

best=data[data['Country_Name']==best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked='true')
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


