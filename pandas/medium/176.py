#99% & 99%
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.drop('id', axis=1, inplace=True)
    reduced_employee = employee[employee['salary'] != employee['salary'].max()]
    second_max_salary = reduced_employee['salary'].max()
    return pd.DataFrame({'SecondHighestSalary': [second_max_salary]})