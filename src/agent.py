import pandas as pd
import pandasai as pai
from pandasai import Agent, SmartDataframe

employees_data = {
    "EmployeeID": [1, 2, 3, 4, 5],
    "Name": ["John", "Emma", "Liam", "Olivia", "William"],
    "Department": ["HR", "Sales", "IT", "Marketing", "Finance"],
}

salaries_data = {
    "EmployeeID": [1, 2, 3, 4, 5],
    "Salary": [5000, 6000, 4500, 7000, 5500],
}

employees_df = SmartDataframe(employees_data)
salaries_df = SmartDataframe(salaries_data)

print(employees_df)
print(salaries_df)

# agent = Agent([employees_df, salaries_df], memory_size=10)

# Chat with the agent
response = salaries_df.chat("What is the highest salary?")
print(response)
