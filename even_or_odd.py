# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.




def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    
print(even_or_odd(3))
print(even_or_odd(2))