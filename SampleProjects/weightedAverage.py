nums = [18.5, 16.0, 15.0, 16.0, 12.0, 19.0, 12.0, 14.5]
weigths = [3, 2, 3, 2, 2, 1, 3, 3]

# Calculate total of weights
weighted_sum = sum(num * weight for num, weight in zip(nums, weigths))
totla_weight = sum(weigths)

# Calculate weighted average of numbers
weighted_average = weighted_sum / totla_weight

print(f"The weighted average of numbers is {weighted_average:.2f}")