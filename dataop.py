import pandas as pd


data = {
    'Name': ['Amit', 'Priya', 'Ravi', 'Sneha', 'Raj'],
    'Age': [25, 28, 22, 24, 27],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing'],
    'Salary': [50000, 55000, 48000, 52000, 58000]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)


print("\nFirst 2 rows:\n", df.head(2))
print("\nLast 2 rows:\n", df.tail(2))


print("\nDataFrame Info:")
print(df.info())

print("\nStatistical Summary:\n", df.describe())


print("\nEmployee Names:\n", df['Name'])


print("\nName and Salary Columns:\n", df[['Name', 'Salary']])


filtered = df[df['Age'] > 24]
print("\nEmployees with Age > 24:\n", filtered)


sorted_df = df.sort_values(by='Salary', ascending=False)
print("\nSorted by Salary (Descending):\n", sorted_df)


df['Bonus'] = df['Salary'] * 0.10
print("\nDataFrame after adding Bonus column:\n", df)


df.loc[df['Name'] == 'Ravi', 'Salary'] = 49000
print("\nDataFrame after updating Ravi's Salary:\n", df)


df.drop('Bonus', axis=1, inplace=True)
print("\nDataFrame after deleting Bonus column:\n", df)


grouped = df.groupby('Department')['Salary'].mean()
print("\nAverage Salary by Department:\n", grouped)


df.to_csv('employee_data.csv', index=False)
print("\nData saved to 'employee_data.csv'")
