

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    factor = 1
    if n == 1:
        return 1
    elif n > 1:
        factor = n * factorial(n-1)
    return factor


if __name__ == '__main__':

    n = int(input().strip())

    result = factorial(n)

    print(result)
