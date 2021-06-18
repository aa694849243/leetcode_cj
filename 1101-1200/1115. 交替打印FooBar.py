# -*- coding: utf-8 -*-


# 我们提供一个类：
#
#
# class FooBar {
#   public void foo() {
#     for (int i = 0; i < n; i++) {
#       print("foo");
#     }
#   }
#
#   public void bar() {
#     for (int i = 0; i < n; i++) {
#       print("bar");
#     }
#   }
# }
#
#
#  两个不同的线程将会共用一个 FooBar 实例。其中一个线程将会调用 foo() 方法，另一个线程将会调用 bar() 方法。
#
#  请设计修改程序，以确保 "foobar" 被输出 n 次。
#
#
#
#  示例 1:
#
#
# 输入: n = 1
# 输出: "foobar"
# 解释: 这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，"foobar" 将被输出一次。
#
#
#  示例 2:
#
#
# 输入: n = 2
# 输出: "foobarfoobar"
# 解释: "foobar" 将被输出两次。
#
#  👍 114 👎 0

# 多线程问题
from threading import Lock


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foolock = Lock()
        self.barlock = Lock()
        self.barlock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.foolock.acquire()
            printFoo()
            self.barlock.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.barlock.acquire()
            printBar()
            self.foolock.release()


# 2生产消费问题
import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.printfoo = threading.Semaphore(1)
        self.printbar = threading.Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.printfoo.acquire()  # 缓冲区-1
            printFoo()
            self.printbar.release()  # bard的缓冲区+1

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.printbar.acquire()
            printBar()
            self.printfoo.release()


# 3 threading condition
# https://leetcode-cn.com/problems/print-foobar-alternately/solution/python3-condition-by-zhengbinchen/
class FooBar:
    def __init__(self, n):
        self.n = n
        self.con = threading.Condition()
        self.t = 0

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            if self.con.acquire():
                if self.t == 1:
                    self.con.wait()

                printFoo()
                self.t = 1
                self.con.notify()
                self.con.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            if self.con.acquire():
                if self.t == 0:
                    self.con.wait()

                printBar()
                self.t = 0
                self.con.notify()
                self.con.release()
