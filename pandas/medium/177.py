import pandas as pd

#OPTION 1
def nth_highest_salary1(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.drop('id', axis=1, inplace=True)
    unique_salaries = employee['salary'].drop_duplicates()
    sorted_salaries = unique_salaries.sort_values(ascending=False)

    if N>0 and N <= len(sorted_salaries):
        return pd.DataFrame({f'getNthHighestSalary({N})': [sorted_salaries.iloc[N-1]]})

    else:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})

#Optimized way, less readable
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N < 1:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    try:
        # Get the Nth highest salary by dropping duplicates and getting the Nth largest value
        nth_salary = employee['salary'].drop_duplicates().nlargest(N).iloc[N-1]
    # If the Nth salary does not exist, return None
    except IndexError:
        nth_salary = None

    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_salary]})