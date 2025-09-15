# Assignment 1: AI-Generated Python Problems
# Name: [Your Name Here]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
I'm learning python in a high school programming class. I have some past experience with Python. 
Can you create 5 practice problems that cover: 
> - Variables and basic data types 
> - Conditionals (if/elif/else) 
> - Loops (for and while) 
> - Functions > - Basic list operations
 Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs.

"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
1. Variables & Basic Data Types – Age Calculator

Task:
Ask the user for their name and birth year. Assume the current year is 2025.
Calculate their age and print:

Hello [name], you are [age] years old.


Example:

Input:
Name: Mia
Birth Year: 2010

Output:
Hello Mia, you are 15 years old.

2. Conditionals – Number Checker

Task:
Ask the user for an integer.

If it’s positive, print "Positive".

If it’s negative, print "Negative".

If it’s zero, print "Zero".
If the number is even, also print "Even". If odd, print "Odd".

Example:

Input: -4
Output:
Negative
Even

3. Loops – Sum of Multiples

Task:
Ask the user for a number n.
Use a for loop to find the sum of all numbers between 1 and n that are multiples of 3 or 5.
Print the sum.

Example:

Input: 10
Output: 33


(Explanation: 3 + 5 + 6 + 9 + 10 = 33)

4. Functions – Temperature Converter

Task:
Write a function c_to_f(celsius) that converts Celsius to Fahrenheit using:

F = (C × 9/5) + 32


Ask the user for a Celsius temperature, call the function, and print the result.

Example:

Input: 0
Output: 32.0

Input: 100
Output: 212.0

5. Lists – Average & Largest Finder

Task:

Ask the user to enter 5 numbers (space-separated).

Store them in a list.

Print the average of the numbers.

Print the largest number.

Example:

Input: 4 8 15 16 23
Output:
Average: 13.2
Largest: 23
"""











# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

from msvcrt import kbhit


print("Testing Problem 1:")
name = input("what is your name ")
birth = int(input("what year were you born "))
age = 2025 - birth
print(f"Hello {name} you are {age} years old")

print("\nTesting Problem 2:")
# Add your tests here
num=int(input("Number:"))

if num > 0:
    print("positive")

elif num < 0:
    print("negative")
else:
    print("zero")

if num % 2 == 0:
    print("even")
else:
    print("odd")

print("\nTesting Problem 3:")
n=int(input("Number:"))
for v in range(1,n):
    print(v)
print("\nTesting Problem 4:")
# Add your tests here
cel = int(input("Temperature in Celsius:"))
far = (cel * 9/5)+32
print(far)


print("\nTesting Problem 5:")
nums = list(map(float, input("Enter 5 numbers: ").split()))
average = sum(nums) / len(nums)
largest = max(nums)
print(f"Average: {average}")
print(f"Largest: {largest}")


