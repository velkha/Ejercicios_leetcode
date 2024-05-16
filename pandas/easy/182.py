
def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicate_emails = person.groupby('email').filter(lambda x: len(x) > 1)
    return duplicate_emails[['email']].drop_duplicates()