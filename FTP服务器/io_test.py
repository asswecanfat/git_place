import os


'''def run_thread(n):
    for i in range(n):
        print(threading.current_thread().name + ',' +str(i))


t1 = threading.Thread(target=run_thread, args=(20,), name='t1')
t2 = threading.Thread(target=run_thread, args=(30,), name='t2')
t1.start()
t2.start()
t1.join()
t2.join()
print('完成')'''
'''class A:
    def a(self, n):
        print(n)
inp = input()
obj = getattr(A(), inp)
obj('n')'''
'''path = r'D:\wps\ftp_root'
print(path.replace(os.path.dirname(path), ''))

dir_count = 0
file_count = 0
def get_all_dir(path, sp="|"):
    # 得到当前目录下所有的文件
    fills_list = os.listdir(path)
    sp += "-"
    # 处理每一个文件
    for file_name in fills_list:
        # 判断是否是路径（用绝对路径）
        file_abs_path = os.path.join(path, file_name)
        if os.path.isdir(file_abs_path):
            global dir_count
            dir_count += 1
            print(sp, "目录：", file_name)
            get_all_dir(file_abs_path, sp)
        else:
            global file_count
            file_count += 1
            print(sp, "普通文件：", file_name)

get_all_dir(path)'''
import  sys
for i in sys.argv:
    print(i)


