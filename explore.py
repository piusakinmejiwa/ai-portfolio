import pandas as pd

MIN_MONTHS = 3

#1. Load the CSV into a DataFrame (a table you can work with in Python)
df = pd.read_csv("policies.csv")

#2. Look at the data

print(df.head())   # first 5 rows
print(df.shape)    # number of rows and columns
print(df.dtypes)   # the type of each column

#3. Add a new column, calculated for every row at once

df["total_paid"] = df["premium"] * df["months_paid"]

#4.  Add a True/False column for at-risk policies
df["at_risk"] = df["months_paid"] < MIN_MONTHS

#5. Filter: keep only the at-risk rows
at_risk_df = df[df["at_risk"]]
print("\nAt-risk policyholders:")
print(at_risk_df[["name", "state", "months_paid", "total_paid"]])

#6. Summary numbers

print(f"\n{len(at_risk_df)} of {len(df)} policies are at risk")
print(f"Total collected: {df['total_paid'].sum()} naira")

# 7. Save the at-risk list to a new file
at_risk_df.to_csv("at_risk.csv", index=False)
print("\nSaved at at_risk.csv")

percentage_at_risk = len(at_risk_df) / len(df) * 100
print(f"{percentage_at_risk:.1f}% of policies are out of risk.")

print(f"{df.groupby("payment_method")["at_risk"].mean().sort_values(ascending=False)}")




