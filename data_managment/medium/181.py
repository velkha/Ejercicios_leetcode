# unoptimized
def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df_merged = employee.merge(employee, left_on='managerId', right_on='id', suffixes=('', '_mgr'))
    result = df_merged[df_merged['salary'] > df_merged['salary_mgr']][['name']]
    result.columns = ['Employee']
    return result

# optimized
def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    manager_salaries = employee[['id', 'salary']]
    manager_salaries.columns = ['managerId', 'managerSalary']
    
    df_merged = employee.merge(manager_salaries, on='managerId')
    
    result = df_merged[df_merged['salary'] > df_merged['managerSalary']][['name']]
    
    result.columns = ['Employee']
    
    return result