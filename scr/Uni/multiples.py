"""
Write a program which prints the multiples of 3 from 3 to 60 (3, 6, 9, 12, 15, 18, 21, 24...)
"""

if __name__ == '__main__':
    # Prints the numbers in format [3, 6, 9, ...] in same line
    print(list(range(3, 61, 3)))

    # Prints the numbers in format {3, 6, 9, ...} in same line
    print(set(range(3, 61, 3)))

    # Prints the numbers in format (3, 6, 9, ...) in same line
    print(tuple(range(3, 61, 3)))


    # Prints every number in same line
    print(*range(3, 61, 3))

    # Prints every number in same line
    for i in range(3, 61, 3):
        print(i, end =" ")

    print('\n')

    # Prints every number in a new line
    for i in range(3, 61, 3):
        print(i)




