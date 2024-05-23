import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Parameters
n = 100
mean = 50
sigma_squared = 30
num_experiments = 100000
degrees_of_freedom = n - 1

# Simulate the experiments
y_values = []

for _ in range(num_experiments):
    # Generate a sample
    sample = np.random.normal(mean, np.sqrt(sigma_squared), n)
    # Calculate the sample mean
    sample_mean = np.mean(sample)
    # Calculate the sample variance
    sample_variance = np.var(sample, ddof=1)
    # Calculate Y
    y = (sample_mean - mean)/ np.sqrt(sample_variance / n)
    y_values.append(y)

# Plot the distribution of Y
plt.hist(y_values, bins=20, density=True, alpha=0.6, color='g', label='Simulation')

# Plot the t-distribution
x = np.linspace(-4, 4, 100)
t_dist = t.pdf(x, df=degrees_of_freedom)
plt.plot(x, t_dist, 'r-', lw=2, label=f't-distribution (df={degrees_of_freedom})')

# Add labels and legend
plt.xlabel('Y')
plt.ylabel('Density')
plt.title('Distribution of Y and t-distribution')
plt.legend()
plt.show()