
def factorial(num):
    """
    Computes the factorial of num
    :param num:
    :return: the factorial of num
    """
    r = 1
    for i in range(num):
        r *= (i + 1)

    return r

