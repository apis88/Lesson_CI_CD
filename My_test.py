from My_function  import square
def test(number):
    s = square(number)

    test_s = number ** 2

    assert s == test_s

def test2(number):
    s = square(number)

    test_s2 = number * number

    assert s == test_s2


test(10)
test(1)
test(40)
test2(10)
test2(1)
test2(40)