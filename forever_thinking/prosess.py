from time import sleep

def progress(percent: int=0, width: int=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']', f' {percent:.0f}%', sep='', end='', flush=True)

for i in range(101):
    progress(i)
