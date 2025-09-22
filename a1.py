"""
MY ORIGINAL AI PROMPT:
[Paste the prompt you used to generate your problem set here]
I'm learning python in a high school programming class. I have some past experience with Python. 
Can you create 5 practice problems that cover: 
> - Variables and basic data types 
> - Conditionals (if/elif/else) 
> - Loops (for and while) 
> - Functions > - Basic list operations
 Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs.

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: [Problem Title/Description]
[Copy the complete problem description from your AI assistant]
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
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
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

print("Testing Problem 1:")
# Add your tests here
name = input("what is your name ")
birth = int(input("what year were you born "))
age = 2025 - birth
print(f"Hello {name} you are {age} years old")

print("\nTesting Problem 2:")
# Add your tests here
num=int(input("Number:"))

print("\nTesting Problem 3:")
# Add your tests here
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
# Add your tests here
nums = list(map(float, input("Enter 5 numbers: ").split()))
average = sum(nums) / len(nums)
largest = max(nums)
print(f"Average: {average}")
print(f"Largest: {largest}")