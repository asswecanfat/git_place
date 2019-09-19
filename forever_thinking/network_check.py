import psutil
from time import sleep


def check_internet(sec: int):
    for i in range(sec):
        d1 = psutil.net_io_counters().bytes_recv
        sleep(1)
        d2 = psutil.net_io_counters().bytes_recv
        if d2 - d1 >= 1024**2:
            print('\r下载速度：', str(round((d2 - d1) / 1024**2, 2)), ' Mb/s', sep='', end='', flush=True)
        elif d2 - d1 >= 1024**3:
            print('\r下载速度：', str(round((d2 - d1) / 1024**3, 2)), ' Gb/s', sep='', end='', flush=True)
        else:
            print('\r下载速度：', str(round((d2 - d1) / 1024, 2)), ' kb/s', sep='', end='', flush=True)

if __name__ == '__main__':
    check_internet(5000)
