'''from tqdm import tqdm
import time
import random
import threading


def test_po():
    a = range(10)
    for i in tqdm(a):
        time.sleep(random.random())
    # print('线程%s已完成' % threading.current_thread().name)

t1 = threading.Thread(target=test_po, name='t1')
t2 = threading.Thread(target=test_po, name='t2')
t1.start()
t2.start()
t1.join()
t2.join()
test_po()
test_po()'''

from eprogress import LineProgress, MultiProgressManager
import threading, time


def li_po(proess_mager, sleep_time):
    for i in range(1, 101):
        proess_mager.update(threading.current_thread().name, i)
        time.sleep(sleep_time)

proess_mager = MultiProgressManager()
t1 = threading.Thread(target=li_po, args=(proess_mager, 0.5), name='1')
t2 = threading.Thread(target=li_po, args=(proess_mager, 1), name='2')
proess_mager.put(str(1), LineProgress(total=100, title='1 Thread'))
proess_mager.put(str(2), LineProgress(total=100, title='2 Thread'))
t1.start()
t2.start()
t1.join()
t2.join()

