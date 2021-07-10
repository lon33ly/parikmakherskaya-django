def solve(n):
    sum = 0
    while n != 0:
        last_digit = n % 10
        sum += last_digit
        n = n // 10

    if check_sum(sum) is True:
        return sum

    return solve(sum)


def check_sum(n):
    if n // 10 == 0:
        return True
    return False


print(solve(77))
