# yield 是一个特殊的关键字，用于定义生成器函数（generator function）。它的作用类似于 return，但有本质区别：
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
# 使用生成器
print(f"当前生成：{next(gen)}")
print(f"当前生成：{next(gen)}")
print(f"当前生成：{next(gen)}")

# 抛出 StopIteration 异常
print(f"当前生成：{next(gen)}")

# 使用这样的代码，则不会触发StopIteration 异常，执行下面的代码，需要先注释掉前面的代码
for value in gen:
    print(value)