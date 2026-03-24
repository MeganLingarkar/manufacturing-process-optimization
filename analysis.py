import pandas as pd
import matplotlib.pyplot as plt

# load the csv file
df = pd.read_csv('manufacturing_defect_data.csv')

# make sure Defect Rate is numeric
df['Defect Rate'] = df['Defect Rate'].astype(str).str.replace('%', '', regex=False).astype(float)

# preview the first 5 rows
print('\n--- First 5 Rows ---')
print(df.head())

# basic info
print('\n--- Dataset Info ---')
df.info()

# average defect rate by machine
print('\n--- Average Defect Rate by Machine ---')
print(df.groupby('Machine')['Defect Rate'].mean().sort_values(ascending=False))

# average defect rate by shift
print('\n--- Average Defect Rate by Shift ---')
print(df.groupby('Shift')['Defect Rate'].mean().sort_values(ascending=False))

# total defects by material
print('\n--- Total Defects by Material ---')
print(df.groupby('Material')['Defect Count'].sum().sort_values(ascending=False))

# most common defect types
print('\n--- Most Common Defect Types ---')
print(df['Defect Type'].value_counts())

#average production cost
print('\n--- Average Production Cost by Machine ---')
print(df.groupby('Machine')['Production Cost'].mean().sort_values())

#chart for average defect rate by machine
avg_defect_by_machine = df.groupby('Machine')['Defect Rate'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
avg_defect_by_machine.plot(kind='bar')
plt.title('Average Defect Rate by Machine')
plt.xlabel('Machine')
plt.ylabel('Average Defect Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#shows number of jobs
print('\n--- Total Number of Jobs ---')
print(len(df))

#shows how many jobs were allocated to each machine
print('\n--- Number of Jobs by Machine ---')
print(df['Machine'].value_counts())

#chart for average defect by material
total_defects_by_material = df.groupby('Material')['Defect Count'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
total_defects_by_material.plot(kind='bar')
plt.title('Total Defects by Material')
plt.xlabel('Material')
plt.ylabel('Total Defect Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#chart for most common defects
most_common_defects = df['Defect Type'].value_counts()

plt.figure(figsize=(10, 6))
most_common_defects.plot(kind='bar')
plt.title('Most Common Defect Types')
plt.xlabel('Defect Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#summary table for each machine
print('\n--- Defect Rate and Production Cost by Machine ---')
machine_summary = df.groupby('Machine').agg({
    'Defect Rate': 'mean',
    'Production Cost': 'mean'
}).sort_values('Defect Rate')

print(machine_summary)

#which machine gives the best balance of both
machine_summary['Defect Score'] = machine_summary['Defect Rate'] / machine_summary['Defect Rate'].max()
machine_summary['Cost Score'] = machine_summary['Production Cost'] / machine_summary['Production Cost'].max()
machine_summary['Overall Score'] = 0.7 * machine_summary['Defect Score'] + 0.3 * machine_summary['Cost Score']

print('\n--- Machine Optimization Score ---')
print(machine_summary.sort_values('Overall Score'))