import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    df_merge_difkey = pd.merge(employee, bonus, left_on='empId', right_on='empId', how='outer')
    return (df_merge_difkey[(df_merge_difkey['bonus']<1000) | (df_merge_difkey['bonus'].isnull())])[["name", "bonus"]]