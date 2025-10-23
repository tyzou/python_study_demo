"""
多线程程序如果没有竞争资源处理起来通常也比较简单
当多个线程竞争临界资源的时候如果缺乏必要的保护措施就会导致数据错乱
说明：临界资源就是被多个线程竞争的资源
"""
import time
import threading

from concurrent.futures import ThreadPoolExecutor


class Account(object):
    """银行账户类 - 演示多线程环境下的线程安全问题及解决方案"""

    def __init__(self):
        """初始化银行账户"""
        self.balance = 0.0  # 账户余额，初始为0
        self.lock = threading.Lock()  # 创建线程锁，用于保护临界资源

    def deposit(self, money):
        """
        存款方法 - 演示如何使用锁保护临界资源

        参数:
            money: 要存入的金额
        """
        # 通过锁保护临界资源，确保同一时间只有一个线程能执行此代码块
        with self.lock:  # 获取锁，执行完后自动释放锁
            # 模拟实际的存款操作过程
            new_balance = self.balance + money  # 计算新的余额
            time.sleep(0.001)  # 模拟网络延迟或处理时间，放大并发问题
            self.balance = new_balance  # 更新账户余额


def main():
    """主函数 - 演示多线程并发存款操作"""
    account = Account()  # 创建银行账户实例

    # 创建线程池，最多同时运行10个工作线程
    pool = ThreadPoolExecutor(max_workers=10)

    # 用于存储所有任务的Future对象列表
    futures = []

    # 模拟100次并发存款操作，每次存入1元
    for _ in range(100):
        # 提交存款任务到线程池，每次存入1元
        future = pool.submit(account.deposit, 1)
        futures.append(future)  # 将任务的Future对象添加到列表中

    # 关闭线程池，不再接受新的任务，等待已提交的任务完成
    pool.shutdown()

    # 等待所有存款任务完成
    for future in futures:
        future.result()  # 获取任务执行结果（这里主要是等待任务完成）

    # 输出最终账户余额，由于使用了锁保护，应该为100.0
    print(f"最终余额: {account.balance}")


if __name__ == '__main__':
    main()



