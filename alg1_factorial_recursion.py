def factorial(n):
    # Base case
    if n == 1:
        print(f"Base: {n}! = {n} ")
        return 1

    # Recursive case
    else:
        print(f"Before recursive call: {n}! = {n} * {n - 1}! ")
        result = factorial(n - 1)
        print(f"After recursive call: {n}! = {n} * {n - 1}! ({n - 1}! = {result})")
        return n * result


if __name__ == '__main__':
    f = 6
    print(f"Factorial {f} is {factorial(f)}")
