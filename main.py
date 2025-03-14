import numpy as np

# 1
# Generate 100 random numbers
np.random.seed(42)
random_numbers = np.random.randint(1, 100, 100)

# Find # divisible by 3 and replace with -1
random_numbers[random_numbers % 3 == 0] = -1
print("Modified Random Numbers (Divisible by 3 replaced with -1):")
print(random_numbers)

# 2
matrix_5x5 = np.arange(1, 26).reshape(5, 5)

# Extract every alternate row
alternate_rows = matrix_5x5[::2]
print("\nAlternate Rows from 5x5 Matrix:")
print(alternate_rows)

# 3
# Generate a 10x10 matrix
matrix_10x10 = np.random.randint(1, 100, (10, 10))

# Sort the matrix by the first column
sorted_matrix_10x10 = matrix_10x10[matrix_10x10[:, 0].argsort()]
print("\nSorted 10x10 Matrix by First Column:")
print(sorted_matrix_10x10)

# 4
# Generate synthetic rainfall data
np.random.seed(42)
rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)
rainfall[np.random.choice(365, 100, replace=False)] = 0  # 100 dry days

rainy_days_count = np.sum(rainfall > 0)
heavy_rain_days_percentage = np.sum(rainfall > 5) / 365 * 100

# Finding longest dry spell
dry_spells = np.split(np.where(rainfall == 0)[0], np.where(np.diff(np.where(rainfall == 0)[0]) != 1)[0] + 1)
longest_dry_spell = max(len(spell) for spell in dry_spells)

print("\nRainfall Analysis Results:")
print(f"Rainy Days Count: {rainy_days_count}")
print(f"Heavy Rain Days Percentage: {heavy_rain_days_percentage:.2f}%")
print(f"Longest Dry Spell: {longest_dry_spell} days")

top_10_wettest_days = np.argsort(rainfall)[-10:][::-1]
print("\nTop 10 Wettest Days (Day Indexes):")
print(top_10_wettest_days)

# Compute average rainfall monthly
monthly_rainfall = [np.mean(rainfall[i * 30:(i + 1) * 30]) for i in range(12)]
print("\nAverage Monthly Rainfall (mm):")
print(monthly_rainfall)

sorted_rainfall = np.sort(rainfall)
median_rainfall = np.median(rainfall)
percentile_90th = np.percentile(rainfall, 90)

print("\nRainfall Sorting Analysis:")
print(f"Median Rainfall: {median_rainfall:.4f} mm")
print(f"90th Percentile Rainfall: {percentile_90th:.4f} mm")

structured_rainfall = np.zeros(365, dtype=[('day', 'i4'), ('rainfall', 'f4'), ('is_rainy', 'b1')])
structured_rainfall['day'] = np.arange(1, 366)
structured_rainfall['rainfall'] = rainfall
structured_rainfall['is_rainy'] = rainfall > 0

rainy_days = structured_rainfall[structured_rainfall['is_rainy']]
average_rainfall_rainy_days = np.mean(rainy_days['rainfall'])

sorted_structured_rainfall = np.sort(structured_rainfall, order='rainfall')[-5:]

print("\nStructured Data Analysis:")
print(f"Average Rainfall on Rainy Days: {average_rainfall_rainy_days:.4f} mm")
print("Top 5 Rainiest Days:")
print(sorted_structured_rainfall[::-1])
