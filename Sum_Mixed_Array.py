# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
# Return your answer as a number.
def mix(arr):
    return sum([int(i) for i in arr])
print(mix([9, 3, '7', '3']))