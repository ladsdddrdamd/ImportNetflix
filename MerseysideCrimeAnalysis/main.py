###### REAL WORLD SCENARIO ################################################################################################################
# The aim of this project is going to be a very high-level Exploratory Data of the Merseyside Crime data
# The data is from Summer 2019 & 2020 to enable an analysis to be completed between the two time periods
# I will import the data, clean it, shape it before displaying it.

# Setting up the project by importing packages for the basic python operations
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

df2007_sorted = df2007.sort_values(by=['LSOA code','Crime type'],ascending=True)
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

tc = 0
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
    tc = crime + tc
    #    print(tc)

    # reset the variable for the next line
    Crime = 0

#create a dictionary to stored the value of total crime for Jun 2019
dict_total_by_Month = {"06-2019":tc}

#Create a list to hold the totals in by Month
list_month =[]
list_month_19 =[]
list_month.append(tc)
list_month_19.append(tc)

#after the for loop exists - calidate the structure of the dataframe to ensure the new colums has been added
#print(dfcount1906.head())
#print(dfcount1906.shape)
#print(dfcount1906.columns)
#print(dfcount1906.isnull().sum())

################ July 2019

tc = 0
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
    tc = crime + tc
    #    print(tc)

    # reset the variable for the next line
    Crime = 0

#Append to dictionary the value of total crime for Jul 2020
dict_total_by_Month["07-2019"] = tc
list_month.append(tc)
list_month_19.append(tc)

#print(dfcount1907.head())
#print(dfcount1907.shape)
#print(dfcount1907.columns)
#print(dfcount1907.isnull().sum())

################ August 2019

tc = 0
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
    tc = crime + tc
    #    print(tc)

    # reset the variable for the next line
    Crime = 0

#Append to dictionary the value of total crime for Aug 2019
dict_total_by_Month["08-2019"] = tc
list_month.append(tc)
list_month_19.append(tc)

#print(dfcount1908.head())
#print(dfcount1908.shape)
#print(dfcount1908.columns)
#print(dfcount1908.isnull().sum())

################ June 2020

list_month_20 = []
tc = 0
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
    tc = crime + tc
    #    print(tc)

    # reset the variable for the next line
    Crime = 0

#Append to dictionary the value of total crime for Aug 2020
dict_total_by_Month["06-2020"] = tc
list_month.append(tc)
list_month_20.append(tc)

#print(dfcount2006.head())
#print(dfcount2006.shape)
#print(dfcount2006.columns)
#print(dfcount2006.isnull().sum())

################ July 2020

tc = 0
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
    tc = crime + tc
    #    print(tc)

    # reset the variable for the next line
    Crime = 0

#Append to dictionary the value of total crime for Jun 2020
dict_total_by_Month["07-2020"] = tc
list_month.append(tc)
list_month_20.append(tc)

#print(dfcount2007.head())
#print(dfcount2007.shape)
#print(dfcount2007.columns)
#print(dfcount2007.isnull().sum())

################ August 2020

tc = 0
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
    tc = crime + tc
    #    print(tc)

    # reset the variable for the next line
    Crime = 0

#Append to dictionary the value of total crime for Aug 2020
dict_total_by_Month["08-2020"] = tc
list_month.append(tc)
list_month_20.append(tc)

#print(dfcount2008.head())
#print(dfcount2008.shape)
#print(dfcount2008.columns)
#print(dfcount2008.isnull().sum())

###### ANALYZE DATA - GROUPING TO GET UNIQUE COUNTS #######################################################################################
# For the various datasets - see how many different crime types there were by LSOA - visually inspect result against counts from dfcount dataframe for each period
#print(df1906_sorted.groupby('LSOA code')['Crime type'].value_counts())
#print(dfcount1906.head(10)) # compare with dfcount1906.head() function looking at the total column for an overall count
#print(df1907_sorted.groupby('LSOA code')['Crime type'].value_counts())
#print(dfcount1907.head(10)) # compare with dfcount1907.head() function looking at the total column for an overall count
#print(df1908_sorted.groupby('LSOA code')['Crime type'].value_counts())
#print(dfcount1908.head(10)) # compare with dfcount1908.head() function looking at the total column for an overall count
#print(df2006_sorted.groupby('LSOA code')['Crime type'].value_counts())
#print(dfcount2006.head(10)) # compare with dfcount2006.head() function looking at the total column for an overall count
#print(df2007_sorted.groupby('LSOA code')['Crime type'].value_counts())
#print(dfcount1907.head(10)) # compare with dfcount2007.head() function looking at the total column for an overall count
#print(df2008_sorted.groupby('LSOA code')['Crime type'].value_counts())
#print(dfcount2008.head(10)) # compare with dfcount1908.head() function looking at the total column for an overall count
#Since they match; this means the data has been created successfully

########################### Join the Datasets together to craete a single dataset ###################   Merge dataframes  ####################################

#I want to create a new dataframe called merged totals 2019 - iwill use the concat method

#merging the tables using concat - ignoring the index as it is of no use to me
df2019_Merged = pd.concat([dfcount1906,dfcount1907,dfcount1908],ignore_index=True)
#print(df2019_Merged.head())
#print(df2019_Merged.columns)
#print(df2019_Merged.isnull().sum())
#print(df2019_Merged.shape) # 2719 records - 18 columns - no null value

#verify the record count by viewing the individuals dataframes - it is a count of districts reporting crime so no great variations expected
#print(dfcount1906.shape) # 911 records - 18 columns - no null value
#print(dfcount1907.shape) # 910 records - 18 columns - no null value
#print(dfcount1908.shape) # 908 records - 18 columns - no null value
# success - they match the merge was successful - 2719 vs 2719

df2020_Merged = pd.concat([dfcount2006,dfcount2007,dfcount2008],ignore_index=True)
#print(df2020_Merged.head())
#print(df2020_Merged.columns)
#print(df2020_Merged.isnull().sum())
#print(df2020_Merged.shape) # 2729 records - 18 columns - no null value

#verify the record count by viewing the individuals dataframes - it is a count of districts reporting crime so no great variations expected
#print(dfcount2006.shape) # 911 records - 18 columns - no null value
#print(dfcount2007.shape) # 910 records - 18 columns - no null value
#print(dfcount2008.shape) # 908 records - 18 columns - no null value
# success - they match the merge was successful - 2719 vs 2719

###### PYTHON - FUNCTIONS - NUMPY #######################################################################################
#Create reuseable code to carry out mathemitical operations over collections quickly using Numpy
np2019 = df2019_Merged.to_numpy()
#print (df2019_Merged.columns)
#print(np2019)
#np2019
np_2019_Total = np.sum(np2019[:,17])
#print(np_2019_Total)

# Creating a list of the crime types names
ms_crimes_2019 = list(df2019_Merged)[2:] # List crime types
#print(ms_crimes)

#starting the counter with 2 as I do not want to get the sum of the first few columns
counter = 2

#Define the 2019 dictionary to hold the values fpr
dict_2019_total = {"names":0}
dict_2019_max = {"names":0}
dict_2019_min = {"names":0}
dict_2019_std = {"names":0}

for names in ms_crimes_2019 :
    if names != 'LSOA name' :
        counter = counter + 1
        #print(counter)
        total = np.sum(np2019[:,counter])
        max = np.max(np2019[:,counter])
        min = np.min(np2019[:,counter])
        stdev = np.std(np2019[:,counter])
        #print("Crime Type: " + names + "; Total: " + str(total) + "; Max: " + str(max) + "; Min: " + str(min) + "; stdev: " + str(stdev))

        #Populate the 2019 dictionary with the summary values
        dict_2019_total[names] = total
        dict_2019_max[names] = max
        dict_2019_min[names] = min
        dict_2019_std[names] = stdev

#delete the dictionary initialising values as they are of no value now
del dict_2019_total["names"]
del dict_2019_max["names"]
del dict_2019_min["names"]
del dict_2019_std["names"]
#print(dict_2019_total)
#print(dict_2019_max)
#print(dict_2019_min)
#print(dict_2019_std)

##################### Repeating for 2020

#Create reuseable code to carry out mathemitical operations over collections quickly using Numpy
np2020 = df2020_Merged.to_numpy()
#print (df2020_Merged.columns)
#print(np2020)
#np2020
np_2020_Total = np.sum(np2020[:,17])
#print(np_2020_Total)

# Creating a list of the crime types names
ms_crimes_2020 = list(df2020_Merged)[2:] # List crime types
#print(ms_crimes)

#starting the counter with 2 as I do not want to get the sum of the first few columns
counter = 2

#Define the 2019 dictionary to hold the values fpr
dict_2020_total = {"names":0}
dict_2020_max = {"names":0}
dict_2020_min = {"names":0}
dict_2020_std = {"names":0}

for names in ms_crimes_2020 :
    if names != 'LSOA name' :
        counter = counter + 1
        #print(counter)
        total = np.sum(np2020[:,counter])
        max = np.max(np2020[:,counter])
        min = np.min(np2020[:,counter])
        stdev = np.std(np2020[:,counter])
        #print("Crime Type: " + names + "; Total: " + str(total) + "; Max: " + str(max) + "; Min: " + str(min) + "; stdev: " + str(stdev))

        #Populate the 2020 dictionary with the summary values
        dict_2020_total[names] = total
        dict_2020_max[names] = max
        dict_2020_min[names] = min
        dict_2020_std[names] = stdev

#delete the dictionary initialising values as they are of no value now
del dict_2020_total["names"]
del dict_2020_max["names"]
del dict_2020_min["names"]
del dict_2020_std["names"]
#print(dict_2020_total)
#print(dict_2020_max)
#print(dict_2020_min)
#print(dict_2020_std)

###########  VISUALIZE - SEABORN & MATPLOTLIB  ############################################################################################

list_month_names = ['06-2019','07-2019','08-2019','06-2020','07-2020','08-2020']

######## Line graph - Summer 2019 vs Summer 2020 #########################
"""
list_month_names = ['06-June','07-July','08-Aug']
fig, ax = plt.subplots()
ax.plot(list_month_names,list_month_19, marker="o", linestyle='dotted', color="r",label='2019')
ax.plot(list_month_names,list_month_20, marker="v", linestyle="--", color="b",label='2020')
plt.legend()
ax.set_xlabel("Time (months)")
ax.set_ylabel("Number of Recorded Crimes")
ax.set_title("Recorded Crimes in Merseyside - Summer 2019 vs Summer 2020")
plt.show()
"""

######## Bar graph - Crime by Area 2019 & 2020 #########################
#crime_no = ['Anti-Soc','Byc Tft','Burg','Damage','Drugs','Other','Theft','Weapons','Public Order','Robbery','Shop-Lift', 'Theft frpm person','Vehicle','Violence']
crime_no = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

LSOA = df1908_sorted["Crime type"].unique()
fig, ax = plt.subplots()
for LSOA in ms_crimes_2019:
    if (LSOA not in ["Total", "LSOA name"]) :
        ax.bar(LSOA, df2020_Merged[LSOA].sum())
        #print(df2019_Merged[LSOA].sum())
ax.set_ylabel("Total Crime Numbers")
ax.set_xticklabels(crime_no)
plt.title ("Crimes By Type - Summer 2019")
plt.show()

fig, ax = plt.subplots()
for LSOA in ms_crimes_2020:
    if (LSOA not in ["Total", "LSOA name"]) :
        ax.bar(LSOA, df2020_Merged[LSOA].sum())
        #print(df2020_Merged[LSOA].sum())
ax.set_ylabel("Total Crime Numbers")
ax.set_xticklabels(crime_no)
plt.title ("Crimes By Type - Summer 2020")
plt.show()

