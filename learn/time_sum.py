import time


class TimeSum(object):
    def __init__(self):
        self.time = 0
        self.run_time = 0

    def __enter__(self):  # 当进入with语句时，调用它获取资源
        self.time = time.time()
        return self  # 返回一个类

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.run_time = float(time.time() - self.time)
        if self.run_time > 3600:
            h = self.run_time // 3600
            m = self.run_time % 3600 // 60
            s = self.run_time % 60
            print(f'该代码共用了：{h}h,{m}m,{s:.2f}s')
            return None
        if self.run_time > 60:
            m = self.run_time // 60
            s = self.run_time % 60
            print(f'该代码共用了：{m}m,{s:.2f}s')
            return None
        print(f'该代码使用了：{self.run_time:.2f}s')

    def __repr__(self):
        return f'{self.__name__!r}()'

