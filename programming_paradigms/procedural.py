"""
This paradigm emphasizes on procedure in terms of under lying machine model. 
There is no difference in between procedural and imperative approach. 
It has the ability to reuse the code and it was boon at that time when it was in use because of its reusability.
"""
# Prompt user to enter a number
num = int(input("Enter any Number: "))

fact = 1  # Initialize factorial variable

# Calculate factorial
for i in range(1, num + 1):
    fact = fact * i

# Print the factorial
print("Factorial of", num, "is:", fact)
