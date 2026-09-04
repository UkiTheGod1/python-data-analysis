status = lambda x: 'Positive number' if x > 0 else 'Negative number'
print(status(10))  # Output: 'Positive number'
print(status(-5))  # Output: 'Negative number'

complex_condition = lambda x: x**2 if x < 5 else (x**3 if x > 5 else x)
print(complex_condition(3))  # Output: 9
print(complex_condition(6))  # Output: 216
print(complex_condition(5))  # Output: 5