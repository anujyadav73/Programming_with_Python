# Create a function with two arguments that will return an array of the first n multiples of x.

# Assume both the given number and the number of times to count will be positive numbers greater than 0.

# Return the results as an array or list ( depending on language ).

def count(x,n):
    return [x*i for i in range(1,n+1)]

print(count(2,5))


# Another way to solve the problem

# Solution:

def count(x, n):
    result = []
    for i in range(1, n + 1):
        result.append(x * i)
    return result

print(count(2, 5))