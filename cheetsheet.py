import pandas as pd 


#here we use 
#nunique() and unique
#value_counts
#filtering
#getgroup
#groupby
#isnull and notnull
#rename
#mean 
#std
#var
#str.contains
#and and or
#min and max



df=pd.read_csv("Weather.csv")
#print(df)


#How to Analyze DataFrame?

#.head() it show only staring 5 row if parameter not given

print(df.head())

#.shape() show total number of rows and column
print(df.shape)

#.columns show name of each column
print(df.columns)

#.index provide index of dataframe
print(df.index)

#dtypes show data type of each column
print(df.dtypes)

#.unique() show unique value only apply single column not whole dataframe
print(df['Weather'].unique())

#nunique show can both apply on single and whole dataframe
print(df.nunique())

#.count show non null value in eachcolumn and applied single and whole dataframe
print(df.count())


#value_counts show all unique value with their count and only single column
print(df['Weather'].value_counts())


#info basic information about dataframe
print(df.info)


#find all unique wind speed value in data

#print(df.head())
print(df.nunique())
print(df['Wind Speed_km/h'].nunique())
print(df['Wind Speed_km/h'].unique())


#find number of times when weatehr is clear

#value count()
print(df.Weather.value_counts())

#filtering
print(df[df.Weather=='Clear']) #without dataframe name at start it result boolean

#groupby
print(df.groupby('Weather').get_group('Clear'))



#number of time when wind speed 4km/h

print(df[df['Wind Speed_km/h']==4])#dataframe name without it show boolean


#null value in data
print(df.isnull()) #boolean
print(df.isnull().sum()) #it will show in sum

print(df.notnull())


#reman column name weather of dataframe
print(df.rename(columns={'Weather':'Weather Condition'})) #reman only temprory
#for perment you write -> inplace=True



#mean visiblity value
print(df.Visibility_km.mean())


#standard deviation of presure in data
print(df.Press_kPa.std())


#variance of relative humidity
print(df['Rel Hum_%'].var())#if there is space between then used bracket otherwise above


#instance when snow recorded
print(df['Weather Condition'].value_counts()) #VALUE COUNT

print(df['Weather Conditon']=='Snow') #filtering


print(df[df['Weather Condition'].str.contains('Snow')].head()) #str.contains


#wind speed about 24 vsibity 25
print(df[(df['Wind Speed_km/h']>24) & (df['Visibility_km']==25)])


#mean value of each volumn against weather condition
print(df.groupby('Weather Conditon').mean()) #grop by

print(df.groupby('Weather Condition').min())
print(df.groupby('Weather Condition').max())

#all weather record where codition is fot

print(df['Weather Conditon']=='Fog') #filtering


#all instance weather is clear or visibilty is above

#print(df[(df['Weather Condtion']=='Clear') or (df['Visibilty_km']>40)])


#all instance weather clear and humidity is greater 50 and vsibitly 40

print(df[(df['Weather Condition']=='Clear') & (df['Rel Hum_%']>50) or (df['Visibitly_km'>40])])






