import pandas as pd

df = pd.read_csv("health_data.csv")

print("Original Data:\n", df.head())

# Handle missing values
df.fillna(df.mean(), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned data
df.to_csv("cleaned_health_data.csv", index=False)

print("Cleaned data saved!")