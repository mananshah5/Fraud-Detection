import pandas as pd

all_matched_reversals = pd.read_parquet('all_matched_reversals.parquet')
df_cleaned = pd.read_parquet('df_cleaned.parquet')
remaining_match_df = pd.read_parquet('remaining_match_df.parquet')
all_matched_reversals.to_csv('all_matched_reversals.csv', index=True)
df_cleaned.to_csv('df_cleaned.csv', index=True)
remaining_match_df.to_csv('remaining_match_df.csv', index=True)