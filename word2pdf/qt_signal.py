from PyQt5.QtCore import QObject, pyqtSignal


class QTSignal(QObject):
    text_edit = pyqtSignal(str)         # 传输的文本
    complete = pyqtSignal(bool)         # 转换完成
    haveUpdate = pyqtSignal(bool)       # 有更新
    sureDown = pyqtSignal(bool)         # 已下载更新
    readyInstall = pyqtSignal(bool)     # 准备安装
    returnReply = pyqtSignal(bool)      # 是否更新
    downing = pyqtSignal(bool, int)     # 正在下载更新
    changeIcon = pyqtSignal(bool)           # 改更新的托盘图标