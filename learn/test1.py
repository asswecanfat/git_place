import sys
from time_sum import TimeSum
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    # 获取命令行参数
    with TimeSum():
        app = QApplication(sys.argv)
        # 创建一个窗口
        w = QWidget()
        # 设置窗口大小
        w.resize(300, 150)
        # 修改窗口左上角坐标
        w.move(300, 300)
        # 设置窗口标题
        w.setWindowTitle('第一个ui')
        # 显示窗口
        w.show()
        # 进入程序的主循环，并通过exit函数确保主循环安全结束
        TimeSum().time_print()
        sys.exit(app.exec_())
