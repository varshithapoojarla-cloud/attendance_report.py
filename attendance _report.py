import pandas as pd
import matplotlib.pyplot as plt

# Create data directly
data = {
    "Employee": ["Rahul", "Sneha", "Arjun", "Rahul", "Priya", "Kiran"],
    "Days_Present": [25, 28, 22, 25, None, 20],
    "Department": ["IT", "HR", "Sales", "IT", "Finance", "Support"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Show original data
print("Original Data")
print(df)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df["Days_Present"] = df["Days_Present"].fillna(df["Days_Present"].mean())

# Show cleaned data
print("\nCleaned Data")
print(df)

# Calculate average attendance
average = df["Days_Present"].mean()

print("\nAverage Attendance:", average)

# Create graph
plt.bar(df["Employee"], df["Days_Present"])

plt.xlabel("Employee")
plt.ylabel("Days Present")
plt.title("Attendance Report")

plt.show()