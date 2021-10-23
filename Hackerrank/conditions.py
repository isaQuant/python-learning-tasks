
# This is a comment.

"""
Platform: Hackerrank

Task:
Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird

Input Format:
A single line containing a positive integer, .

Constraints:
1 <= n <= 100

Output Format:
Print Weird if the number is weird. Otherwise, print Not Weird.
"""

if __name__ == '__main__':
    n = 5
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and n >= 2 and n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and n >= 6 and n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")



"""
Recreating the code as a method 
"""

def weirdNumber(n):
    if n % 2 != 0:
        return "Weird"
    elif n % 2 == 0 and n >= 2 and n <= 5:
        return "Not Weird"
    elif n % 2 == 0 and n >= 6 and n <= 20:
        return "Weird"
    elif n % 2 == 0 and n > 20:
        return "Not Weird"
