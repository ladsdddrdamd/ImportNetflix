###### REAL WORLD SCENARIO ################################################################################################################
# The aim of this project is going to be a very high-level Exploratory Data of the Merseyside Crime data
# The data is from Summer 2019 & 2020 to enable an analysis to be completed between the two time periods
# I will import the data, clean it, shape it before displaying it.

# Setting up the project by importing packages for the basic python operations
import numpy as np
import pandas as pd

############### IMPORTING DATA ############################################################################################################

###### IMPORTING JUNE 2019 DATASET ###########################################################################################
# I will start by importing the crime dataset for July 2019 and looking at the first 5 rows to understand the dataset
df1906 = pd.read_csv(r"C:\UCD2021\MerseysideCrimeAnalysis\2019-06-merseyside-street.csv")

# check the shape of the data
#print(df1906.shape)

# print the first 10 rows of the dataset to have a look at the data
#print(df1906.head(10))

# print the tail the last 5 rows of the dataset to have a look at the last records in the dataset
#print(df1906.tail())

# describing the dataset
#print(df1906.describe())

# Print the names of the columns of the dataset
#print(df1906.columns)

# Print the names of the columns of the dataset
#print(df1906.dtypes)

# Check for Null Values and Sum the Null Values
#print(df1906.isnull())
#print(df1906.isnull().sum())

#We are now going to drop the missing values from the columns - decided against this when I saw the results
#df1906 = df1906.dropna(axis=1)

#Next we will check for duplicates
#print(df1906[df1906.duplicated()])

###################### ANALYZING THE DATA - REMOVING IRRELEVANT COLUMNS FROM THE  DATASETS ################################################
# Having evaluated the data the next step is to decide what data is required for the analysis - 'Month', 'LSOA code', 'LSOA name' & 'Crime Type'
# The columns that we do not want from the data set - 'Crime ID', 'Reported by','Falls within', 'Longitude', 'Latitude' & 'Location'
# After the unwanted columns are dropped we will have a clean dataset for June 2019 records
df1906.drop('Crime ID',axis=1,inplace=True)
df1906.drop('Reported by',axis=1,inplace=True)
df1906.drop('Falls within',axis=1,inplace=True)
df1906.drop('Longitude',axis=1,inplace=True)
df1906.drop('Latitude',axis=1,inplace=True)
df1906.drop('Location',axis=1,inplace=True)
df1906.drop('Last outcome category',axis=1,inplace=True)
df1906.drop('Context',axis=1,inplace=True)

#print out the characteristics of the finalised dataset
#print('Shape - June 2019')
#print(df1906.shape)
#print(df1906.columns)
#print(df1906.describe())


###### IMPORTING JULY & AUGUST 2019 DATASET ###########################################################################################
# Repeat the process for July & August 2019 - they will be saved into separate dataframes as June 2019 has been validated
df1907 = pd.read_csv(r"C:\UCD2021\MerseysideCrimeAnalysis\2019-07-merseyside-street.csv")
df1908 = pd.read_csv(r"C:\UCD2021\MerseysideCrimeAnalysis\2019-08-merseyside-street.csv")

# check the shape of the data
#print(df1907.shape)
#print(df1908.shape)

# print the first 5 rows of the dataset to have a look at the data
#print(df1907.head())
#print(df1908.head())

# print the tail the last 5 rows of the dataset to have a look at the last records in the dataset
#print(df1907.tail())
#print(df1908.tail())

# describing the dataset
#print(df1907.describe())
#print(df1908.describe())

# Print the names of the columns of the dataset
#print(df1907.columns)
#print(df1908.columns)

# Print the names of the columns of the dataset
#print(df1907.dtypes)
#print(df1908.dtypes)

# Check for Null Values and Sum the Null Values
#print(df1907.isnull())
#print(df1908.isnull().sum())

#Next we will check for duplicates
#print(df1907[df1907.duplicated()])
#print(df1908[df1908.duplicated()])

###################### ANALYZING THE DATA - REMOVING IRRELEVANT COLUMNS FROM THE  DATASETS ################################################
# Having evaluated the data the next step is to decide what data is required for the analysis - 'Month', 'LSOA code', 'LSOA name' & 'Crime Type'
# The columns that we do not want from the data set - 'Crime ID', 'Reported by','Falls within', 'Longitude', 'Latitude' & 'Location'
# After the unwanted columns are dropped we will have a clean dataset for June 2019 records
df1907.drop('Crime ID',axis=1,inplace=True)
df1907.drop('Reported by',axis=1,inplace=True)
df1907.drop('Falls within',axis=1,inplace=True)
df1907.drop('Longitude',axis=1,inplace=True)
df1907.drop('Latitude',axis=1,inplace=True)
df1907.drop('Location',axis=1,inplace=True)
df1907.drop('Last outcome category',axis=1,inplace=True)
df1907.drop('Context',axis=1,inplace=True)

df1908.drop('Crime ID',axis=1,inplace=True)
df1908.drop('Reported by',axis=1,inplace=True)
df1908.drop('Falls within',axis=1,inplace=True)
df1908.drop('Longitude',axis=1,inplace=True)
df1908.drop('Latitude',axis=1,inplace=True)
df1908.drop('Location',axis=1,inplace=True)
df1908.drop('Last outcome category',axis=1,inplace=True)
df1908.drop('Context',axis=1,inplace=True)

#print out the characteristics of the finalised dataset
#print('Shape - July 2019')
#print(df1907.shape)
#print(df1907.columns)
#print(df1907.describe())

#print('Shape - August 2019')
#print(df1908.shape)
#print(df1908.columns)
#print(df1908.describe())

###### IMPORTING JUNE, JULY & AUGUST 2020 DATASET ###########################################################################################
# Having validated the data for 2019 - I have now imported the data for 2020 - June, July & August
# Repeat the process for June, July & August 2019 - Validating the data as I go
df2006 = pd.read_csv(r"C:\UCD2021\MerseysideCrimeAnalysis\2020-06-merseyside-street.csv")
df2007 = pd.read_csv(r"C:\UCD2021\MerseysideCrimeAnalysis\2020-07-merseyside-street.csv")
df2008 = pd.read_csv(r"C:\UCD2021\MerseysideCrimeAnalysis\2020-08-merseyside-street.csv")


# check the shape of the data
#print(df2006.shape)
#print(df2007.shape)
#print(df2008.shape)

# print the first 5 rows of the dataset to have a look at the data
#print(df2006.head())
#print(df2007.head())
#print(df2008.head())

# print the tail the last 5 rows of the dataset to have a look at the last records in the dataset
#print(df2006.tail())
#print(df2007.tail())
#print(df2008.tail())

# describing the dataset
#print(df2006.describe())
#print(df2007.describe())
#print(df2008.describe())

# Print the names of the columns of the dataset
#print(df2006.columns)
#print(df2007.columns)
#print(df2008.columns)

# Print the names of the columns of the dataset
#print(df2006.dtypes)
#print(df2007.dtypes)
#print(df2008.dtypes)

# Check for Null Values and Sum the Null Values
#print(df2006.isnull())
#print(df2007.isnull())
#print(df2008.isnull().sum())

#Next we will check for duplicates
#print(df2006[df2006.duplicated()])
#print(df2007[df2007.duplicated()])
#print(df2008[df2008.duplicated()])

###################### ANALYZING THE DATA - REMOVING IRRELEVANT COLUMNS FROM THE  DATASETS ################################################
# Having evaluated the data the next step is to decide what data is required for the analysis - 'Month', 'LSOA code', 'LSOA name' & 'Crime Type'
# The columns that we do not want from the data set - 'Crime ID', 'Reported by','Falls within', 'Longitude', 'Latitude' & 'Location'
# After the unwanted columns are dropped we will have a clean dataset for June 2019 records
df2006.drop('Crime ID', axis=1, inplace=True)
df2006.drop('Reported by', axis=1, inplace=True)
df2006.drop('Falls within', axis=1, inplace=True)
df2006.drop('Longitude', axis=1, inplace=True)
df2006.drop('Latitude', axis=1, inplace=True)
df2006.drop('Location', axis=1, inplace=True)
df2006.drop('Last outcome category', axis=1, inplace=True)
df2006.drop('Context', axis=1, inplace=True)

df2007.drop('Crime ID',axis=1,inplace=True)
df2007.drop('Reported by',axis=1,inplace=True)
df2007.drop('Falls within',axis=1,inplace=True)
df2007.drop('Longitude',axis=1,inplace=True)
df2007.drop('Latitude',axis=1,inplace=True)
df2007.drop('Location',axis=1,inplace=True)
df2007.drop('Last outcome category',axis=1,inplace=True)
df2007.drop('Context',axis=1,inplace=True)

df2008.drop('Crime ID',axis=1,inplace=True)
df2008.drop('Reported by',axis=1,inplace=True)
df2008.drop('Falls within',axis=1,inplace=True)
df2008.drop('Longitude',axis=1,inplace=True)
df2008.drop('Latitude',axis=1,inplace=True)
df2008.drop('Location',axis=1,inplace=True)
df2008.drop('Last outcome category',axis=1,inplace=True)
df2008.drop('Context',axis=1,inplace=True)

#print out the characteristics of the finalised dataset
#print('Shape - June 2020')
#print(df2006.shape)
#print(df2006.columns)
#print(df2006.describe())

#print('Shape - July 2020')
#print(df2007.shape)
#print(df2007.columns)
#print(df2007.describe())

#print('Shape - August 2020')
#print(df2008.shape)
#print(df2008.columns)
#print(df2008.describe())

###################### ANALYZING THE DATA - SORTING THE DATASETS ##########################################################################
# Next I want to sort the data to made it easier to interpret
df1906_sorted = df1906.sort_values(by=['LSOA code','Crime type'],ascending=True)
# validate the change has been made
#print("June 2019")
#print(df1906_sorted.head(10))

df1907_sorted = df1907.sort_values(by=['LSOA code','Crime type'],ascending=True)
#print("July 2019")
#print(df1907_sorted.head(10))

df1908_sorted = df1908.sort_values(by=['LSOA code','Crime type'],ascending=True)
#print("August 2019")
#print(df1908_sorted.head(10))

df2006_sorted = df2006.sort_values(by=['LSOA code','Crime type'],ascending=True)
#print("June 2020")
#print(df2006_sorted.head(10))

df2007_sorted = df1907.sort_values(by=['LSOA code','Crime type'],ascending=True)
#print("July 2020")
#print(df2007_sorted.head(10))

df2008_sorted = df2008.sort_values(by=['LSOA code','Crime type'],ascending=True)
#print("August 2020")
#print(df2008_sorted.head(10))


###### ANALYZING DATA _ DROPPING DUPLICATES THROUGH CHANGING THE TABLE ORIENTATATION #########################################################
# This will allow me to count the instances of crimes accross the LOSA areas

#manipulate the data by creating a column for each crime type
dfcount1906 = pd.crosstab([df1906_sorted['Month'], df1906_sorted['LSOA code'],df1906_sorted['LSOA name'] ], df1906_sorted['Crime type'])
dfcount1906.reset_index(inplace=True)
# validate the change has been made & that there are no null values
# #print(dfcount1906.head())
#print(dfcount1906.shape)
#print(dfcount1906.columns)
#print(dfcount1906.isnull().sum())

dfcount1907 = pd.crosstab([df1907_sorted['Month'], df1907_sorted['LSOA code'],df1907_sorted['LSOA name'] ], df1907_sorted['Crime type'])
dfcount1907.reset_index(inplace=True)
#print(dfcount1907.head())
#print(dfcount1907.shape)
#print(dfcount1907.columns)
#print(dfcount1907.isnull().sum())

dfcount1908 = pd.crosstab([df1908_sorted['Month'], df1908_sorted['LSOA code'],df1908_sorted['LSOA name'] ], df1908_sorted['Crime type'])
dfcount1908.reset_index(inplace=True)
#print(dfcount1908.head())
#print(dfcount1908.shape)
#print(dfcount1908.columns)
#print(dfcount1908.isnull().sum())

dfcount2006 = pd.crosstab([df2006_sorted['Month'], df2006_sorted['LSOA code'],df2006_sorted['LSOA name'] ], df2006_sorted['Crime type'])
dfcount2006.reset_index(inplace=True)
#print(dfcount2006.head())
#print(dfcount2006.shape)
#print(dfcount2006.columns)
#print(dfcount2006.isnull().sum())

dfcount2007 = pd.crosstab([df2007_sorted['Month'], df2007_sorted['LSOA code'],df2007_sorted['LSOA name'] ], df2007_sorted['Crime type'])
dfcount2007.reset_index(inplace=True)
#print(dfcount2007.head())
#print(dfcount2007.shape)
#print(dfcount2007.columns)
#print(dfcount2007.isnull().sum())

dfcount2008 = pd.crosstab([df2008_sorted['Month'], df2008_sorted['LSOA code'],df2008_sorted['LSOA name'] ], df2008_sorted['Crime type'])
dfcount2008.reset_index(inplace=True)
#print(dfcount2008.head())
#print(dfcount2008.shape)
#print(dfcount2008.columns)
#print(dfcount2008.isnull().sum())

###### GET THHE TOTAL COUNT THE INSTANCES OF CRIME TYPE BY LOSA REGION #######   LOOPING WITH ITERROWS#####################################

#tc = 0
Crime = 0
for val, row in dfcount1906.iterrows() :
    #populating the crime int variable
    crime = row["Anti-social behaviour"] + row["Bicycle theft"] + row["Burglary"] + row["Criminal damage and arson"] + \
            row["Drugs"] + row["Other crime"] + row["Other theft"] + row["Possession of weapons"] + row[
                "Public order"] + row["Robbery"] + row["Shoplifting"] + row["Theft from the person"] + row[
                "Vehicle crime"] + row["Violence and sexual offences"]

    # creating a series on every itteration  for June 2019 & add a column called Total
    dfcount1906.loc[val, "Total"] = crime

    # validate the variable is populating collectly for each LOSA & that there are no null values
    #    print(crime)
    #    tc = crime + tc
    #    print(tc)

    # reset the variable for the next line
    Crime = 0

#after the for loop exists - calidate the structure of the dataframe to ensure the new colums has been added
#print(dfcount1906.head())
#print(dfcount1906.shape)
#print(dfcount1906.columns)
#print(dfcount1906.isnull().sum())

################ July 2019

#tc = 0
Crime = 0
for val, row in dfcount1907.iterrows() :
    #populating the crime int variable
    crime = row["Anti-social behaviour"] + row["Bicycle theft"] + row["Burglary"] + row["Criminal damage and arson"] + \
            row["Drugs"] + row["Other crime"] + row["Other theft"] + row["Possession of weapons"] + row[
                "Public order"] + row["Robbery"] + row["Shoplifting"] + row["Theft from the person"] + row[
                "Vehicle crime"] + row["Violence and sexual offences"]

    # creating a series on every itteration for July 2019 & add a column called Total
    dfcount1907.loc[val, "Total"] = crime
    #    print(crime)
    #    tc = crime + tc
    #    print(tc)

    # reset the variable for the next line
    Crime = 0

#print(dfcount1907.head())
#print(dfcount1907.shape)
#print(dfcount1907.columns)
#print(dfcount1907.isnull().sum())

################ August 2019

#tc = 0
Crime = 0
for val, row in dfcount1908.iterrows() :
    #populating the crime int variable
    crime = row["Anti-social behaviour"] + row["Bicycle theft"] + row["Burglary"] + row["Criminal damage and arson"] + \
            row["Drugs"] + row["Other crime"] + row["Other theft"] + row["Possession of weapons"] + row[
                "Public order"] + row["Robbery"] + row["Shoplifting"] + row["Theft from the person"] + row[
                "Vehicle crime"] + row["Violence and sexual offences"]

    # creating a series on every itteration for August 2019 & add a column called Total
    dfcount1908.loc[val, "Total"] = crime
    #    print(crime)
    #    tc = crime + tc
    #    print(tc)

    # reset the variable for the next line
    Crime = 0

#print(dfcount1908.head())
#print(dfcount1908.shape)
#print(dfcount1908.columns)
#print(dfcount1908.isnull().sum())

################ June 2020

#tc = 0
Crime = 0
for val, row in dfcount2006.iterrows() :
    #populating the crime int variable
    crime = row["Anti-social behaviour"] + row["Bicycle theft"] + row["Burglary"] + row["Criminal damage and arson"] + \
            row["Drugs"] + row["Other crime"] + row["Other theft"] + row["Possession of weapons"] + row[
                "Public order"] + row["Robbery"] + row["Shoplifting"] + row["Theft from the person"] + row[
                "Vehicle crime"] + row["Violence and sexual offences"]

    # creating a series on every itteration for June 2020 & add a column called Total
    dfcount2006.loc[val, "Total"] = crime
    #    print(crime)
    #    tc = crime + tc
    #    print(tc)

    # reset the variable for the next line
    Crime = 0

#print(dfcount2006.head())
#print(dfcount2006.shape)
#print(dfcount2006.columns)
#print(dfcount2006.isnull().sum())

################ July 2020

#tc = 0
Crime = 0
for val, row in dfcount2007.iterrows() :
    #populating the crime int variable
    crime = row["Anti-social behaviour"] + row["Bicycle theft"] + row["Burglary"] + row["Criminal damage and arson"] + \
            row["Drugs"] + row["Other crime"] + row["Other theft"] + row["Possession of weapons"] + row[
                "Public order"] + row["Robbery"] + row["Shoplifting"] + row["Theft from the person"] + row[
                "Vehicle crime"] + row["Violence and sexual offences"]

    # creating a series on every itteration for July 2020 & add a column called Total
    dfcount2007.loc[val, "Total"] = crime
    #    print(crime)
    #    tc = crime + tc
    #    print(tc)

    # reset the variable for the next line
    Crime = 0

#print(dfcount2007.head())
#print(dfcount2007.shape)
#print(dfcount2007.columns)
#print(dfcount2007.isnull().sum())

################ August 2020

Crime = 0
for val, row in dfcount2008.iterrows() :
    #populating the crime int variable
    crime = row["Anti-social behaviour"] + row["Bicycle theft"] + row["Burglary"] + row["Criminal damage and arson"] + \
            row["Drugs"] + row["Other crime"] + row["Other theft"] + row["Possession of weapons"] + row[
                "Public order"] + row["Robbery"] + row["Shoplifting"] + row["Theft from the person"] + row[
                "Vehicle crime"] + row["Violence and sexual offences"]

    # creating a series on every itteration for August 2020 & add a column called Total
    dfcount2008.loc[val, "Total"] = crime
    #    print(crime)
    #    tc = crime + tc
    #    print(tc)

    # reset the variable for the next line
    Crime = 0

#print(dfcount2008.head())
#print(dfcount2008.shape)
#print(dfcount2008.columns)
#print(dfcount2008.isnull().sum())

###### ANALYZE DATA - GROUPING TO GET UNIQUE COUNTS #######################################################################################
# For the various datasets - see how many different crime types there were by LSOA - visually inspect result against counts from dfcount dataframe for each period
#print(df1906_sorted.groupby('LSOA code')['Crime type'].value_counts())
#print(dfcount1906.head(10)) # compare with dfcount1906.head() function looking at the total column for an overall count
#print(df1907_sorted.groupby('LSOA code')['Crime type'].value_counts())
#print(dfcount1907.head(10)) # compare with dfcount1906.head() function looking at the total column for an overall count
#print(df1908_sorted.groupby('LSOA code')['Crime type'].value_counts())
#print(dfcount1908.head(10)) # compare with dfcount1906.head() function looking at the total column for an overall count
#print(df2006_sorted.groupby('LSOA code')['Crime type'].value_counts())
#print(dfcount2006.head(10)) # compare with dfcount1906.head() function looking at the total column for an overall count
#print(df2007_sorted.groupby('LSOA code')['Crime type'].value_counts())
#print(dfcount1907.head(10)) # compare with dfcount1906.head() function looking at the total column for an overall count
#print(df2008_sorted.groupby('LSOA code')['Crime type'].value_counts())
#print(dfcount2008.head(10)) # compare with dfcount1906.head() function looking at the total column for an overall count

#Since they match; this means the data has been created successfully

########################### Join the Datasets together to craete a single dataset ###################   Merge dataframes  ####################################
"""

# For June 2019 - see how many different crime types there were
#print(df1906_sorted['Crime type'].nunique())
#print(df1906_sorted.groupby('LSOA code')['Crime type'].value_counts())

# Now I want to add a new dataframe to capture a line for just each LSOA by crime type
df1906_unique = df1906_sorted.drop_duplicates(subset=["LSOA code","Crime type"])
#print (df1906_unique.head(5))
#print (df1906_unique.shape)

#print (df1906_unique.shape)
#print(df1906_unique[["LSOA code","Crime type"]])
df1906_unique["Count"] = 0



#add a column containing a count of the crimnes by crimetypw within the LSOA
#df1906_value_counts = df1906_sorted.groupby('LSOA code')['Crime type'].value_counts()
#print (df1906_value_counts.head(5))
#print (df1906_value_counts.shape)


#for i, row in df1906_unique.iterrows():
#    print(i)

# Merge the two Dataframes
#df1906_unique.merge(df1906_value_counts, on='LSOA code')
#print (df1906_unique.head(5))
#print (df1906_unique.shape)


#As the count total match I can join the two datasets to get a count of the crime by district
#df1906_final = df1906_unique.merge(df1906_value_counts, on='LSOA code')
#print (df1906_final.head(20))
#print (df1906_final.shape)




"""
#print(df1907_sorted['Crime type'].nunique())
#print(df1908_sorted['Crime type'].nunique())
#print(df2006_sorted['Crime type'].nunique())
#print(df2007_sorted['Crime type'].nunique())
#print(df2008_sorted['Crime type'].nunique())

#print(df1906_sorted.groupby('LSOA code')['Crime type'].sum())

#Next Step is to create summarised data by LSOA & region by crime type
"""
"""
