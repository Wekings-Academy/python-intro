from python_basics import classify_grade, sum_of_even, guess_number

# Test for classify_grade
def test_classify_grade():
    assert classify_grade(95) == "优秀"
    assert classify_grade(80) == "良好"
    assert classify_grade(65) == "及格"
    assert classify_grade(40) == "不及格"

# Test for sum_of_even
def test_sum_of_even():
    assert sum_of_even([1, 2, 3, 4, 5]) == 6
    assert sum_of_even([0, 8, 11, 14]) == 22
    assert sum_of_even([]) == 0

# Test for guess_number
def test_guess_number():
    assert guess_number(5, [1, 3, 5]) == "猜对了！"
    assert guess_number(10, [2, 4, 6]) == "很遗憾，没猜中。"
    assert guess_number(7, [7]) == "猜对了！"
