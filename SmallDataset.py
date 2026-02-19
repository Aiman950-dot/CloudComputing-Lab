import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for plots
sns.set_style("darkgrid")

# Create a simple dataset
data = {
    'Fruits': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'Quantity': [10, 15, 7, 5, 12],
    'Price': [2, 1, 3, 4, 5]
}

df = pd.DataFrame(data)

# Display the dataset
print("Here is our dataset:\n")
print(df)

# Plot: Bar chart of Fruits vs Quantity
plt.figure(figsize=(8,5))
sns.barplot(x='Fruits', y='Quantity', data=df, palette="viridis")
plt.title("Fruit Quantity Comparison 🍎🍌🍒")
plt.show()

# Plot: Scatter plot of Quantity vs Price
plt.figure(figsize=(8,5))
sns.scatterplot(x='Quantity', y='Price', data=df, s=100, color='red')
plt.title("Quantity vs Price 💰")
plt.xlabel("Quantity")
plt.ylabel("Price")
plt.show()
