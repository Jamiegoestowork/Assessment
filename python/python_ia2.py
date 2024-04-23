# -*- coding: utf-8 -*-
"""python_IA2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gAf7qQUP3t9uhWLC_T-RERMZxBibnzgJ
"""

import numpy as np
import pandas as pd

#1

arr = np.array([1,2,3,4,5])

arr_max = np.max(arr)
print(arr_max)
arr_min = np.min(arr)
print(arr_min)
arr_sum = np.sum(arr)
print(arr_sum)
arr_std = np.std(arr)
print(arr_std)

#2
health_data = np.array([[160, 70, 30],   # height, weight, age for individual 1
                        [165, 65, 35],   # height, weight, age for individual 2
                        [170, 75, 40]])  # height, weight, age for individual 3

print(health_data)

#3

student_scores = np.array([[98,100,99,97],
                           [76,99,-1,-1]])

print(np.mean(student_scores[:,-3:],axis=1))

#4
temp_readings = np.linspace(15,25,20,endpoint=True)
print(temp_readings)

#5
import numpy as np
daily_closing_prices = np.array([100, 102, 98, 105, 107, 110, 108, 112, 115, 118, 120])
window_size = 5

#6
mean_vector = np.array([0,0])
covariance_matrix = np.array([[1,0.5],
                              [0.5,2]])

#7
import numpy as np
properties_matrix = np.array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]])
determinant = np.linalg.det(properties_matrix)
print(determinant)

#8
array_2d = np.random.randint(10,size=(3,3))
condition = array_2d>5
print(array_2d)
print('------------')
result = array_2d[condition]
print(result)

#9
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Age': [25, 30, 35, 40, 45, 50, 55],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Miami', 'Boston'],
        'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales', 'IT', 'HR']}

df = pd.DataFrame(data)

result = df[(df['Age']<45) & (df['Department'] != 'HR')][['Name','City']]
print(result)

#10
data = {'Department': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Home Goods'],
        'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Sales': [70000, 50000, 30000, 40000, 60000]}

sales_df = pd.DataFrame(data)

grouped_sales_data = sales_df.groupby(['Department','Salesperson'])['Sales'].agg(['mean'])
print(grouped_sales_data)

#11
data = {
    'Product': ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Flour', 'Grapes'],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit', 'Bakery', 'Fruit'],
    'Price': [1.20, 0.50, 3.00, 2.50, 4.00, 1.50, 2.00],
    'Promotion': [True, False, True, True, False, True, False]
}

fruits_df = pd.DataFrame(data)
print(fruits_df)

xoxo = fruits_df.groupby('Category')['Price'].agg(['mean']).tail(1)
print(xoxo)

result = fruits_df[(fruits_df['Price']>2.2) & (fruits_df['Promotion']==False)]
print(result)

#12
employee_data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'IT', 'Finance', 'IT'],
    'Manager': ['John', 'Rachel', 'Emily', 'Rachel']
}

# Dataset of employee project assignments
project_data = {
    'Employee': ['Alice', 'Charlie', 'Eve'],
    'Project': ['P1', 'P3', 'P2']
}


employee_df = pd.DataFrame(employee_data)
project_df = pd.DataFrame(project_data)

result_df = project_df.merge(employee_df,how='outer',on='Employee' )
print(result_df)

#13
sports_df = pd.read_csv('/content/Q13_sports_team_stats.csv')
sports_df['winratio'] = sports_df['Wins']/sports_df['GamesPlayed']

print(sports_df)
#we cannot calculate avg score as we dont know scores in each mactch so i just added winration column

#14
customer_df = pd.read_csv('/content/Q14_customer_purchases.csv')
print(customer_df.head())

#15
studentgrades_df = pd.read_csv('/content/Q15_student_grades.csv')
print(studentgrades_df.head())

least_grades_sub = studentgrades_df.groupby(['Subject'])['Grade'].agg(['mean']).sort_values('mean').head(1)
print(least_grades_sub)
#we can focus on history subject as it has less average marks compared to other subjects
