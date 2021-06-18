# -*- coding: utf-8 -*-


# 假设有这么一个类：
#
#  class ZeroEvenOdd {
#   public ZeroEvenOdd(int n) { ... }      // 构造函数
#   public void zero(printNumber) { ... }  // 仅打印出 0
#   public void even(printNumber) { ... }  // 仅打印出 偶数
#   public void odd(printNumber) { ... }   // 仅打印出 奇数
# }
#
#
#  相同的一个 ZeroEvenOdd 类实例将会传递给三个不同的线程：
#
#
#  线程 A 将调用 zero()，它只输出 0 。
#  线程 B 将调用 even()，它只输出偶数。
#  线程 C 将调用 odd()，它只输出奇数。
#
#
#  每个线程都有一个 printNumber 方法来输出一个整数。请修改给出的代码以输出整数序列 010203040506... ，其中序列的长度必须为 2n
# 。
#
#
#
#  示例 1：
#
#  输入：n = 2
# 输出："0102"
# 说明：三条线程异步执行，其中一个调用 zero()，另一个线程调用 even()，最后一个线程调用odd()。正确的输出为 "0102"。
#
#
#  示例 2：
#
#  输入：n = 5
# 输出："0102030405"
#
#  👍 100 👎 0
# 多线程问题
import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zerolock = threading.Lock()
        self.evenlock = threading.Lock()
        self.oddlock = threading.Lock()
        self.oddlock.acquire()
        self.evenlock.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.zerolock.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.oddlock.release()
            else:
                self.evenlock.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 2 == 0:
                self.evenlock.acquire()
                printNumber(i)
                self.zerolock.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            if i%2:
                self.oddlock.acquire()
                printNumber(i)
                self.zerolock.release()
