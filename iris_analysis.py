# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the dataset with error handling
try:
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map(dict(enumerate(iris.target_names)))
    print("Dataset loaded successfully.\n")
except Exception as e:
    print("Failed to load the dataset:", e)
    exit()

# Display the first few rows
print("First 5 rows of the dataset:\n", df.head(), "\n")

# Data structure and missing values
print("Data types:\n", df.dtypes, "\n")
print("Missing values:\n", df.isnull().sum(), "\n")

# Clean dataset (no missing values in Iris, but here's how you would handle it)
# df = df.dropna()  # OR df.fillna(method='ffill', inplace=True)

# Task 2: Basic Data Analysis
print("Basic statistics:\n", df.describe(), "\n")

# Group by species and compute the mean of numerical columns
grouped = df.groupby('species').mean()
print("Mean values grouped by species:\n", grouped, "\n")

# Task 3: Data Visualization

# Set seaborn style
sns.set(style="whitegrid")

# Line Chart (not typically time series in Iris, so we'll simulate trend)
df_sorted = df.sort_values(by=iris.feature_names[0])
plt.figure(figsize=(8, 4))
plt.plot(df_sorted[iris.feature_names[0]].values, label=iris.feature_names[0])
plt.title("Simulated Line Chart: Sepal Length Trend")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.tight_layout()
plt.show()

# Bar Chart: Average petal length per species
plt.figure(figsize=(6, 4))
sns.barplot(x='species', y='petal length (cm)', data=df)
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()

# Histogram: Distribution of Sepal Width
plt.figure(figsize=(6, 4))
sns.histplot(df['sepal width (cm)'], bins=10, kde=True)
plt.title("Histogram of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(6, 4))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.tight_layout()
plt.show()

# Observations / Insights
print("Observations:")
print("- Setosa tends to have shorter petal length and sepal length.")
print("- Petal length increases significantly for Virginica compared to Versicolor.")
print("- Sepal width has a normal distribution, but with variation between species.")
print("- Clear positive correlation between sepal and petal lengths for some species.\n")
