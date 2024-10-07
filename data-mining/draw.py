import pandas as pd

# Load the compressed CSV file
df = pd.read_csv('data-mining/data/task2_dataset.csv.gz', compression='gzip')

# Save it as a regular CSV file
df.to_csv('task2_dataset.csv', index=False)
