# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set seaborn style for better visuals
sns.set(style="whitegrid")

# Task 1: Load and Explore the Dataset

try:
    # Load Iris dataset
    iris = load_iris(as_frame=True)
    df = iris.frame  # Convert to pandas DataFrame
    print("✅ Dataset loaded successfully.")
except Exception as e:
    print(f"❌ Failed to load dataset: {e}")
    exit()

# Display the first few rows
print("\n📄 First 5 rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\n🔍 Data Types and Missing Values:")
print(df.info())

# Check for missing values
missing = df.isnull().sum()
print("\n🧹 Missing values in each column:")
print(missing)

# Clean dataset (Iris has no missing values, but include logic)
if missing.any():
    df = df.dropna()
    print("🧹 Missing values dropped.")
else:
    print("✅ No missing values detected.")

# Task 2: Basic Data Analysis

print("\n📊 Descriptive Statistics:")
print(df.describe())

# Grouping by species and getting mean of numerical columns
grouped_means = df.groupby("target")[
    ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
].mean()

# Map target numbers to species names
species_map = dict(zip(range(3), iris.target_names))
df['species'] = df['target'].map(species_map)
grouped_means.index = iris.target_names

print("\n📈 Mean values grouped by species:")
print(grouped_means)

# Task 3: Data Visualization

# Line Chart: Petal length over sample index (by species)
plt.figure(figsize=(10, 5))
for species in iris.target_names:
    subset = df[df['species'] == species]
    plt.plot(subset.index, subset['petal length (cm)'], label=species)
plt.title("Petal Length Over Samples by Species")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.tight_layout()
plt.show()

# Bar Chart: Average Sepal Length per Species
plt.figure(figsize=(8, 5))
sns.barplot(x=grouped_means.index, y=grouped_means['sepal length (cm)'])
plt.title("Average Sepal Length per Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.tight_layout()
plt.show()

# Histogram: Distribution of Petal Length
plt.figure(figsize=(8, 5))
sns.histplot(df['petal length (cm)'], bins=20, kde=True, color='teal')
plt.title("Distribution of Petal Length")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Scatter Plot: Sepal Length vs. Petal Length
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="sepal length (cm)",
    y="petal length (cm)",
    hue="species",
    palette="deep"
)
plt.title("Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()
