# Anne Tran (UCID: 30286177)
# Assign 2_Q5

import pandas as pd
import numpy as np

df=pd.read_csv("student.csv") # load dataset into dataframe

def classifyGrade(grade): # classify the grade into 3 categories
    if grade<=9:
        return "Low"
    elif grade >=15:
        return "High"
    else:
        return "Medium"

df["grade_band"]=df["grade"].apply(classifyGrade) # use .apply() to classify the grade in to 3 categories (high, low and medium)

# Create summary table
summaryTable=df.groupby("grade_band").agg(
    numberOfStudent=("grade", "count"), # count number of grade for each category
    averageAbsense=("absences", "mean"), # calculate the average absence of each category
    percentInternet=("internet", "mean")) # calculate the average of student access to internet
summaryTable["percentInternet"]*=100 # calculate the percentage of student access to internet

summaryTable.to_csv("student_bands.csv", index=False) # save summary table into a new csv file

