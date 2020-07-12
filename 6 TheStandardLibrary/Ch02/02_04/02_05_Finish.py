# Statistics Module
import statistics
import math

# our Data for kids at a summer camp
agesData = [10, 13, 14, 12, 11, 10, 11, 10, 15]

# Mean: Average, Sum/number of inputs
print('Mean:', statistics.mean(agesData))

# Mode: Most Frequent Value
print('Mode:', statistics.mode(agesData))

# Median: Midpoint
print('Median:', statistics.median(agesData))

print('Sorting...', sorted(agesData))

# Variance: How Varied is our data, is it a lot or pretty close together
print('Variance:', statistics.variance(agesData))

# Standard Deviation, The Square Root of our Variance
print('Standard Deviation:', statistics.stdev(agesData))

# doing the Deviation ourselves, for testing
print(math.sqrt(statistics.variance(agesData)))
