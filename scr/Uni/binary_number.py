
def binary_to_decimal(string):
    """
    Converts a binary number to decimal
    :param string: the binary number
    :return: the decimal number of
    """







def check_binary_number(string):
    """
    Checks if the given number is a binary number
    :param string: a number
    :return: true if the given number is a binary number
    """
    for c in string:
        if c != 0 and c != 1:
            return False
    return True

# return Anweisung ohne Rueckgabewert entsprcht return None
# it is possible to return more than one value
