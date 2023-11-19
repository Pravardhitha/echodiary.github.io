import matplotlib.pyplot as plt
import pandas as pd

# Sample data preparation
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Anger': [2, 1, 3],
    'Happiness': [5, 7, 4],
    'Sadness': [1, 2, 1]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(df['Date'], df['Anger'], label='Anger', marker='o')
plt.plot(df['Date'], df['Happiness'], label='Happiness', marker='o')
plt.plot(df['Date'], df['Sadness'], label='Sadness', marker='o')

plt.xlabel('Date')
plt.ylabel('Emotion Intensity')
plt.title('Emotional Health Trends Over Time')
plt.legend()
plt.grid(True)
plt.show()
