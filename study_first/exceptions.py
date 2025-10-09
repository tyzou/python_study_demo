# 异常处理示例

# 基本的try-except
try:
    number = int(input("请输入一个数字："))
    result = 100 / number
    print(f"100除以{number}等于{result}")
except ValueError:
    print("错误：请输入一个有效的数字")

except ZeroDivisionError:
    print("错误：不能除以零")

except Exception as e:
    print(f"发生了其他错误{e}")

else:
    print("计算成功完成！")

finally:
    print("无论是否发生异常，这里都会执行")


class AgeError(Exception):
    """当年龄不符合要求时抛出的异常"""
    pass

def verify_age(age):
    if age < 0:
        raise AgeError("年龄不能为负数")
    if age > 150:
        raise AgeError("年龄不可能大于150岁")
    return True

# 测试自定义异常
try:
    verify_age(200)
except AgeError as e:
    print(e)
