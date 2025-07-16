import sys
sys.path.append("D:\\code\\python-intro1")
from pathlib import Path

# 获取项目根目录
root_dir = Path(__file__).parent.parent  
sys.path.append(str(root_dir))  # 添加根目录到模块搜索路径

# 导入被测试的函数
from python_basics import classify_grade, sum_of_even, guess_number

# 测试 classify_grade 函数
def test_classify_grade():
    # 正常情况
    assert classify_grade(95) == "优秀", "95分应判定为优秀"
    assert classify_grade(85) == "良好", "85分应判定为良好"
    assert classify_grade(75) == "及格", "75分应判定为及格"
    assert classify_grade(55) == "不及格", "55分应判定为不及格"
    
    # 边界值
    assert classify_grade(90) == "优秀", "90分应判定为优秀"
    assert classify_grade(80) == "良好", "80分应判定为良好"
    assert classify_grade(60) == "及格", "60分应判定为及格"
    assert classify_grade(59) == "不及格", "59分应判定为不及格"
    
    # 极限值
    assert classify_grade(100) == "优秀", "100分应判定为优秀"
    assert classify_grade(0) == "不及格", "0分应判定为不及格"

# 测试 sum_of_even 函数
def test_sum_of_even():
    # 正常情况
    assert sum_of_even([1, 2, 3, 4, 5]) == 6, "偶数和应为 2+4=6"
    assert sum_of_even([10, 23, 44, 57]) == 54, "偶数和应为 10+44=54"
    
    # 空列表
    assert sum_of_even([]) == 0, "空列表的偶数和应为0"
    
    # 全奇数
    assert sum_of_even([1, 3, 5]) == 0, "全奇数列表的偶数和应为0"
    
    # 全偶数
    assert sum_of_even([2, 4, 6]) == 12, "全偶数列表的偶数和应为12"
    
    # 包含0（0是偶数）
    assert sum_of_even([0, 1, 3]) == 0, "包含0的列表的偶数和应为0"

# 测试 guess_number 函数
def test_guess_number():
    # 数字在列表中
    assert guess_number(5, [1, 3, 5]) == "猜对了！", "数字5在列表中"
    assert guess_number(0, [0, 1, 2]) == "猜对了！", "数字0在列表中"
    
    # 数字不在列表中
    assert guess_number(4, [1, 3, 5]) == "很遗憾，没猜中。", "数字4不在列表中"
    
    # 空列表
    assert guess_number(5, []) == "很遗憾，没猜中。", "空列表中无法猜中任何数字"
    
    # 列表中有重复元素
    assert guess_number(3, [3, 3, 3]) == "猜对了！", "重复元素不影响判断"
    
    # 负数测试
    assert guess_number(-2, [-3, -2, -1]) == "猜对了！", "负数在列表中"
    assert guess_number(2, [-3, -2, -1]) == "很遗憾，没猜中。", "正数不在负数列表中"