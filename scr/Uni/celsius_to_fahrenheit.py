
def celsius_to_fahrenheit(c):
    """
    Method to convert celsius to fahrenheit
    :param c: celsius
    :return: fahrenheit
    """
    return c * 1.8 + 32

"""
Main to execute method
"""
if __name__ == '__main__':
    c = float(input())
    print(celsius_to_fahrenheit(c))

