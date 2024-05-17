def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = customers.merge(orders, left_on='id', right_on='customerId', how='left')
    never_ordered_df = merged_df[merged_df['customerId'].isna()]
    return never_ordered_df[['name']].rename(columns={'name': 'Customers'})