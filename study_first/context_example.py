"""
上下文管理器版计时器
用法：
    with Timer() as t:
        do_something()
执行完毕后会自动打印耗时
"""
import time  # 提供 time.time() 和 time.sleep()


class Timer:
    """
        一个“上下文管理器”（Context Manager）类。
        只要实现了 __enter__ / __exit__ 这两个魔术方法，
        就能被 with 语句自动调用，从而完成“进入-清理”两段逻辑。
    """

    # 进入上下文：with 语句开始执行时，解释器会最先跑到这里
    def __enter__(self):
        print("开始计时...")
        self.start = time.time() # 浮点型，单位秒，精度一般到微秒
        return self # 不返回也行，但返回 self 更灵活

    # 离开上下文：with 语句的代码块执行完毕（哪怕中间抛异常）都会跑到这里
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
           参数解释（由解释器自动传入）：
               exc_type : 异常类型（如 ZeroDivisionError），无异常则为 None
               exc_val  : 异常实例，无异常则为 None
               exc_tb   : 异常的 traceback 对象，无异常则为 None

           返回值：
               返回 True  表示“异常已被处理，外部不要再抛”；
               返回 False 或 None 表示“异常未被处理，继续向外抛”。
               这里我们不做异常吞掉，所以直接隐式返回 None。
        """
        print("结束计时...")
        self.end = time.time()
        elapsed = self.end - self.start
        print(f"耗时: {elapsed:.2f}秒")

        # 小技巧：如果你想把耗时再往外抛，可以:
        # self.elapsed = elapsed
        # 然后在 with 外面通过 t.elapsed 读取

# 3. 使用contextlib模块创建上下文管理器
from contextlib import contextmanager

@contextmanager
def database_connection(db_name):
    """使用contextlib创建的数据库连接上下文管理器"""
    print(f"连接到数据库: {db_name}")
    connection = f"数据库连接对象: {db_name}"  # 模拟数据库连接

    try:
        yield connection  # 返回连接对象给with语句
    except Exception as e:
        print(f"数据库操作出错: {e}")
    finally:
        print(f"关闭数据库连接: {db_name}")

if __name__ == "__main__":
    # with 是一个用于上下文管理的关键字，主要作用是自动管理资源
    with Timer() as t:
        time.sleep(1)
        print("正在执行任务...")

    # 使用contextlib创建的上下文管理器
    print("测试数据库连接上下文管理器:")
    with database_connection("school_db") as conn:
        print(f"使用{conn}进行数据操作")

