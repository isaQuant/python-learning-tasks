"""
Task:
The provided code stub reads two integers from STDIN, a and b.

Add code to print three lines where:
1.The first line contains the sum of the two numbers.
2.The second line contains the difference of the two numbers (first - second).
3.The third line contains the product of the two numbers.

Example:
    a=3
    b=5

Print the following:
    8
    -2
    15

Input format:
The first line contains the first integer, a.
The second line contains the second integer, b.

Constraints:
1 <= a <= 10^10
1 <= b <= 10^10

Output format:
Print the three lines as explained above.
"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    if 1 <= a <= 10^10 and 1 <= b <= 10^10:
        print(a+b)
        print(a-b)
        print(a*b)
    else:
        print("The input number must be >= 1 and <= 10^10")