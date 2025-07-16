from python_basics import classify_grade, sum_of_even, guess_number

# 测试 classify_grade 函数：根据分数判断等级
def test_classify_grade():
    """
    测试 classify_grade 函数，验证不同分数对应的等级判断是否正确。
    预期规则：
        - 90 及以上：优秀
        - 80-89：良好
        - 60-79：及格
        - 60 以下：不及格
    """
    assert classify_grade(95) == "优秀", "95分应判定为优秀"
    assert classify_grade(80) == "良好", "80分应判定为良好"
    assert classify_grade(65) == "及格", "65分应判定为及格"
    assert classify_grade(40) == "不及格", "40分应判定为不及格"


# 测试 sum_of_even 函数：计算列表中偶数的和
def test_sum_of_even():
    """
    测试 sum_of_even 函数，验证不同输入列表的偶数和计算是否正确。
    逻辑：遍历列表，累加其中的偶数（能被2整除的数）。
    """
    # 常规列表，包含多个偶数、奇数
    assert sum_of_even([1, 2, 3, 4, 5]) == 6, "列表[1,2,3,4,5]的偶数和应为 2+4=6"
    # 列表包含0（0是偶数）、多位数偶数、奇数
    assert sum_of_even([0, 8, 11, 14]) == 22, "列表[0,8,11,14]的偶数和应为 0+8+14=22"
    # 空列表，偶数和应为0
    assert sum_of_even([]) == 0, "空列表的偶数和应为0"


# 测试 guess_number 函数：判断数字是否在列表中
def test_guess_number():
    """
    测试 guess_number 函数，验证数字与列表匹配时的结果是否正确。
    逻辑：检查目标数字是否在候选列表中，返回对应提示语。
    """
    # 数字在列表中（列表含多个元素）
    assert guess_number(5, [1, 3, 5]) == "猜对了！", "数字5在列表[1,3,5]中，应提示'猜对了！'"
    # 数字不在列表中（列表含多个元素）
    assert guess_number(10, [2, 4, 6]) == "很遗憾，没猜中。", "数字10不在列表[2,4,6]中，应提示'很遗憾，没猜中。'"
    # 数字在列表中（列表仅含目标数字）
    assert guess_number(7, [7]) == "猜对了！", "数字7在列表[7]中，应提示'猜对了！'"