import pandas as pd

#Load your dataset
df = pd.read_csv('Police Data.csv')

print("\n Q. 1) Instruction (For Data Cleaning) - Remove the column that only contains missing values ")
df.dropna(axis=1, how='all', inplace=True)
print(" Output : Dropped columns with all missing values \n")

print(" \n Q. 2) Question (Based on Filtering + Value Counts) - For Speeding, were Men or Women stopped more often?")
#Filter rows where violation is speeding
speeding_stops = df[df['violation'] == 'Speeding']

#Count the occurrences of each gender"
gender_counts = speeding_stops['driver_gender'].value_counts()

print("The result is :")
print(gender_counts)

print("\n Q. 3) Question (Groupby) - Does gender affect who gets searched during a stop? ")
# Group by gender and count the searches
search_counts_by_gender = df.groupby('driver_gender')['search_conducted'].sum()

print("  result ---")
print(search_counts_by_gender)

print("\n Q. 4) Question (Mapping + Data-Type Casting) - What is the mean stop_duration? ")
print(" Map stop durations to numeric values")
df['stop_duration'] = df['stop_duration'].map({'0-15 Min': 7.5, '16-30 Min': 23, '30+ Min': 45})

#Convert stop duration to numeric dtype
df['stop_duration'] = pd.to_numeric(df['stop_duration'], errors='coerce')

#Calculate the mean stop duration
mean_stop_duration = df['stop_duration'].mean()

print("mean stop_duration is :")
print(mean_stop_duration)

print("\n Q. 5) Question (Groupby, Describe) - Compare the age distributions for each violation ")
#Group by violation and describe the age column
age_distribution_by_violation = df.groupby('violation')['driver_age'].describe()

print("  Comparasion the age distributions for each violation \n ")
print(age_distribution_by_violation)
