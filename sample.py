def sum(num1, num2):
    return num1 + num2


def sum_only_positive(num1, num2):
    if num1 > 0 and num2 > 0:
        return num1 + num2
    else:
        return None


if __name__ == "__main__":
    print(sum(2, 4))
    print(sum_only_positive(2, 4))
    print(sum_only_positive(-1, 3))

