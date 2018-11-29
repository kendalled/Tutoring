# Import statements
import numpy as np
import matplotlib.pyplot as plt


# Starting Variables
mu, sigma, n, replications = 8.25, 0.75, 5, 30
mean_Array = []

# Random Normal Variable
# Efficient because 'sample' variable is reused every iteration
for i in range(replications):
    sample = np.random.normal(mu, sigma, n)
    print("Averaging " + str(len(sample)) + " new samples...")
    # Finds the mean of the 5 samples, adds to array
    mean_Array.append(np.mean(sample))

# Prints out array containing 500 averages (one average for every replication)
print("\n Array of Means: ")
print(mean_Array)

# Plots and shows mean_Array on histogram
plt.hist(mean_Array, range=[7,10])
plt.show()
