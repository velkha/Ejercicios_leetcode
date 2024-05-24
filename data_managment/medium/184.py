import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(employee, department, left_on='departmentId', right_on='id', suffixes=('', '_dept'))

    max_salary_df = merged_df.groupby('name_dept')['salary'].max().reset_index()

    result_df = pd.merge(merged_df, max_salary_df, left_on=['name_dept', 'salary'], right_on=['name_dept', 'salary'])
    result_df = result_df[['name_dept', 'name', 'salary']]
    result_df.columns = ['Department', 'Employee', 'Salary']

    return result_df