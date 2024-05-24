import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs = logs.sort_values(by='id').reset_index(drop=True)
    consecutive_nums = set()
    for i in range(len(logs) - 2):
        if (logs.loc[i, 'num'] == logs.loc[i + 1, 'num'] == logs.loc[i + 2, 'num'] and 
            logs.loc[i + 1, 'id'] == logs.loc[i, 'id'] + 1 and 
            logs.loc[i + 2, 'id'] == logs.loc[i + 1, 'id'] + 1):
            consecutive_nums.add(logs.loc[i, 'num'])
    result = pd.DataFrame(list(consecutive_nums), columns=['ConsecutiveNums'])

    return result