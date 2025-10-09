# 基本示例 functions.py
def greet(name):
    """向指定的打招呼"""
    return f"你好,{name}!"

print(greet("张三"))

def power(x,n=2):
    """计算x的n次方"""
    return x ** n

print(f"2的平方,{power(2)}")
print(f"2的3次方,{power(2,3)}")

# 可变参数
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(f"1+2+3的和:{sum_numbers(1,2,3)}")
print(f"1到5的和：{sum_numbers(1,2,3,4,5)}")

# 关键字参数
def build_profile(name,age,**kwargs):
    """创建一个包含用户信息的字典"""
    profile = {"name":name,"age":age}
    profile.update(kwargs)
    return profile

user = build_profile("张伟",30,occupation="工程师",city="北京",hobby="读书")
print(f"用户信息{user}")