import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:

    unique_cities = insurance.groupby(['lat', 'lon']).filter(lambda x: len(x) == 1)

    shared_tiv_2015 = insurance.groupby('tiv_2015').filter(lambda x: len(x) > 1)['tiv_2015'].unique()

    result = unique_cities[unique_cities['tiv_2015'].isin(shared_tiv_2015)]

    total_tiv_2016 = round(result['tiv_2016'].sum(), 2)
    return pd.DataFrame({'tiv_2016': [total_tiv_2016]})