def is_prime(func):
    def wrapped(*num: int):
        result = func(*num)
        for n in range(2, result):
            if result % n == 0:
                print("Составное")
                return result
            else:
                print("Простое")
                return result
    return wrapped
@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)