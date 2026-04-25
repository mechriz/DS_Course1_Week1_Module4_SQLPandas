# CodeGrade step0
# Run this cell without changes

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandasql import sqldf


# CodeGrade step1

df = pd.read_csv('titanic.csv', index_col=0)

# Look at first 5 rows
df.head()

# CodeGrade step2
# Replace None with your code

women_and_children_df = df[(df['Sex'] == 'female') | (df['Age'] <= 15)]
adult_males_df = df[(df['Sex'] == 'male') & (df['Age'] > 15)]

# CodeGrade step3
# Replace None with your code

first_class_df = df[df['Pclass'] == 1]
second_third_class_df = df[df['Pclass'] != 1]

# CodeGrade step4
# Replace None with your code

query_string = "PassengerId >= 500"
high_passenger_number_df = df.query(query_string)

# Looking at first 5 rows
high_passenger_number_df.head()

# CodeGrade step5
# Replace None with your code

query_string = "Sex == 'female' or Age <= 15"
female_children_df = df.query(query_string)

# Looking at first 5 rows
female_children_df.head()

# CodeGrade step6
# Replace None with your code

df = df.eval('Age_x_Fare = Age * Fare')

# Looking at first 5 rows, should see new column
df.head()

# CodeGrade step7
# Replace None with your code

pysqldf = lambda q: sqldf(q, globals())

# CodeGrade step8
# Replace None with your code

query1 = "SELECT Name FROM df LIMIT 10"

passenger_names = pysqldf(query1)
passenger_names

# CodeGrade step9
# Replace None with your code

query2 = "SELECT Name, Fare FROM df WHERE Sex = 'male' AND Survived = 1 LIMIT 30"

sql_surviving_males = pysqldf(query2)
sql_surviving_males

# CodeGrade step10
# Replace None with your code

query3 = """
    SELECT Pclass, COUNT(*) 
    FROM df 
    WHERE Sex = 'female' AND Survived = 1 
    GROUP BY Pclass
"""
query4 = """
    SELECT Pclass, COUNT(*) 
    FROM df 
    WHERE Sex = 'female' AND Survived = 0 
    GROUP BY Pclass
"""

survived_females_by_pclass_df = pysqldf(query3)
died_females_by_pclass_df = pysqldf(query4)