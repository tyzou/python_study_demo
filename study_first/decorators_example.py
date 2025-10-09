import time
from functools import wraps

# 最简单的装饰器
def my_decorator(func):
    # 使用*args和**kwargs接收任意参数
    def wrapper(*args, **kwargs):
        print("装饰器添加的内容：函数执行前")
        # 执行原函数
        func(*args, **kwargs)
        print("装饰器添加的内容：函数执行后")
    return wrapper

# 1. 最简单的装饰器：打印函数执行信息
def simple_decorator(func):
    @wraps(func)  # 保留原函数信息
    def wrapper():
        print(f"准备执行 {func.__name__} 函数")
        func()  # 执行原函数
        print(f"{func.__name__} 函数执行完毕")
    return wrapper

@my_decorator
def say_hello(num):
    print(f"Hello world,输入的内容：{num}")

@my_decorator
@simple_decorator
def helloworld():
    print("hello 你好啊。(执行无参数)")

say_hello(11)
print("\n\n")
helloworld()