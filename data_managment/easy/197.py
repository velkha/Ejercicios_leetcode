import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    weather = weather.sort_values(by='recordDate')
    weather['day_diff'] = weather['recordDate'].diff().dt.days
    weather['prev_temperature'] = weather['temperature'].shift(1)
    weather['prev_temperature'] = weather['prev_temperature'].where(weather['day_diff'] == 1, other=None)
    result = weather[weather['temperature'] > weather['prev_temperature']]
    return result[['id']]