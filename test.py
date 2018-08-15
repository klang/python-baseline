from sample import sum, sum_only_positive

def test_sum():
    assert sum(5, 5) == 10


def test_sum_positive_ok():
    assert sum_only_positive(2, 2) == 4


def test_sum_positive_fail():
    assert sum_only_positive(-1, 2) is None


if __name__ == "__main__":
    test_sum()
    test_sum_positive_ok()
    test_sum_positive_fail()
    #print(sum(2, 4))
    #print(sum_only_positive(2, 4))
    #print(sum_only_positive(-1, 3))
