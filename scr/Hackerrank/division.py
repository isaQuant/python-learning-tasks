"""
Task:
    The provided code stub reads two integers, a and b from STDIN.

    Add logic to print two lines. The first line should contain the result of integer division,  a // b .
    The second line should contain the result of float division, a /b .

    No rounding or formatting is necessary.

Example:
    a = 3
    b = 5

    The result of integer division 3//5 = 0
    The result of the float division 3/5 = 0.6

    Print:
    0
    0.6

Input format:
    The first line contains the first integer, a.
    The second line contains the second integer, b.

Output format:
    Print the two lines as described above.

"""

from __future__ import division

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a//b)
    print(a/b)

