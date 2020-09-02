from PyQt5 import QtGui
from UI import Ui_MainWindow as MainForm
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QApplication
from PyQt5.QtCore import QThreadPool
from pathlib import Path
from sys_tray import AppTray
from thread_work import FileThread, UpdateCheck, UpdateGet, UpdateInstall
from config_read import ReadConfig
from loguru import logger
from datetime import date
# import win32api  # winapi库
# import win32con  # windows常数定义
import sys
# import psutil

logger.add(f'logs/{str(date.today())}',  # 日志
           level='DEBUG',
           format='{time:YYYY-MM-DD HH:mm:ss}',
           rotation='10 MB')
file_fillter = ['.doc', '.docx']


@logger.catch
def read_qss(qss_file: str):
    with open(qss_file, 'r') as f:
        return f.read()


class MainUI(QMainWindow, MainForm):
    def __init__(self):
        super(MainUI, self).__init__()
        self.config = ReadConfig()
        self.taryShow = self.config.read_isHide()  # 控制进入原来的主窗口退出
        self.setupUi(self)
        self.set_style()
        self.files_list = []
        self._connect()
        self.threadpool = QThreadPool()
        self.set_missionLable_icon()
        self.textEdit.dragEnterEvent = lambda a0: self._textEdit_dragEnterEvent(a0)
        self.textEdit.dropEvent = lambda a0: self._textEdit_dropEvent(a0)
        # 转换状态线程初始化
        self.th_pr = FileThread()
        # 更新检查子线程的初始化
        self.update = UpdateCheck(float(self.config.read_version()))
        # 更新下载子线程的初始化
        self.update_get = UpdateGet()
        print(self.taryShow)

        # 禁用主窗口的关闭,实际上还是会触发closeEvent
        self.tray = AppTray(self)
        self.thread_work_deal()
        QApplication.setQuitOnLastWindowClosed(self.taryShow)

    def _textEdit_dragEnterEvent(self, a0: QtGui.QDragEnterEvent) -> None:
        if a0.mimeData().hasText():
            a0.accept()
        else:
            a0.ignore()

    def _textEdit_dropEvent(self, a0: QtGui.QDropEvent) -> None:
        path_urls = [i.url().replace('file:///', '') for i in a0.mimeData().urls()
                     if Path(i.url()).suffix in file_fillter]
        if path_urls:  # 判断是否拖拽的是过滤器里的文件
            text = ';'.join(path_urls)
            self.files_list.extend(path_urls)
            self.config.change_path(Path(path_urls[0]).parent)
            self.lineEdit.setText(text)
            self.lineEdit.setCursorPosition(0)  # 设置文字光标

    def thread_work_deal(self):
        # 线程销毁(实为等到该线程结束销毁类实例)
        self.th_pr.setAutoDelete(False)
        self.update.setAutoDelete(False)
        self.update_get.setAutoDelete(False)
        # 转换状态线程连接
        self.th_pr.text_signal.text_edit.connect(self.text_print)
        self.th_pr.text_signal.complete.connect(self.turn_end)
        # 更新检查线程连接
        self.update.signal.haveUpdate.connect(self.check_update)
        # 更新下载线程连接
        self.update_get.signal.downing.connect(self.update_progress)
        self.update_get.signal.sureDown.connect(self.ready_install)
        # 托盘程序修改图标
        self.th_pr.text_signal.changeIcon.connect(self.tray.dealFile_set_icon)

    def _connect(self):  # 信号连接
        self.pushButton_2.clicked.connect(self._get_files)  # 获取文件
        self.pushButton.clicked.connect(self.thread_print)  # 开线程避免堵塞ui
        self.action.triggered.connect(self.about_frame)  # 说明框
        self.actionhelp.triggered.connect(self.thread_update)  # 点击下载

    def set_missionLable_icon(self):  # 设置窗口图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('static/pic/main_ui.ico'),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def set_style(self):  # 样式
        self.pushButton.setProperty('name', 'pushButton')  # 设置属性映射
        self.pushButton_2.setProperty('name', 'pushButton_2')
        qss = read_qss('static/qss/style.qss')
        self.label_2.setText(f"version:{self.config.read_version()}")
        self.pushButton_2.setStyleSheet(qss)
        self.pushButton.setStyleSheet(qss)
        self.setStyleSheet(qss)
        self.lineEdit.setStyleSheet(qss)
        self.textEdit.setStyleSheet(qss)

    def _get_files(self):  # 从文件选择框中获取文件列表
        self.lineEdit.clear()
        files_names, ok = QFileDialog.getOpenFileNames(self.centralwidget,
                                                       "选取多个文件",
                                                       self.config.read_chiose_path(),
                                                       "Text Files (*.doc);;Text Files (*.docx)")
        if files_names:  # 判断是否选取
            files_names_line = ';'.join([i for i in files_names])
            self.files_list.extend([i for i in files_names])
            self.config.change_path(Path(files_names[0]).parent)
            self.lineEdit.setText(files_names_line)
            self.lineEdit.setCursorPosition(0)

    def set_button(self, state: bool):  # 设置按钮状态
        self.pushButton.setEnabled(state)
        self.pushButton_2.setEnabled(state)

    def text_print(self, string):
        self.textEdit.append(string)

    def turn_first(self):  # 转换开始
        self.textEdit.clear()
        self.set_button(False)
        self.pushButton.setText('转换中......')

    def turn_end(self, tf):  # 转换结束
        if tf:
            self.pushButton.setText('转换')
            self.set_button(True)
            self.lineEdit.clear()
            self.files_list.clear()

    def thread_print(self):  # 开启子线程打印工作状态
        self.turn_first()
        self.th_pr.update_file_list(self.files_list)
        self.threadpool.start(self.th_pr)

    def thread_update(self):  # 开启子线程进行更新
        self.actionhelp.setEnabled(False)  # 开始更新前禁用此选项
        self.threadpool.start(self.update)

    def check_update(self, b):
        if b:
            reply = QMessageBox.question(self.centralwidget, '提示', '有新的更新，是否更新？',
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                if exist := [i for i in self.config.read_file_save_path().glob('*.zip')]:
                    self.ready_install(bool(exist))
                else:
                    self.threadpool.start(self.update_get)
        else:
            QMessageBox.about(self.centralwidget, '提醒', '已是最新版本！')
            self.actionhelp.setEnabled(True)  # 准备安装开启此选项

    def update_progress(self, dowing: bool, progress: int):
        self.updatelabel.setText(f'正在下载:{progress}%' if dowing else '')

    def ready_install(self, ready: bool):
        if ready:
            reply = QMessageBox.question(self.centralwidget, '提示', '更新包已下载完成，是否更新',
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                up_install = UpdateInstall()
                self.threadpool.start(up_install)
            self.actionhelp.setEnabled(True)  # 准备安装开启此选项

    def about_frame(self):
        QMessageBox.about(self.centralwidget, "关于", "此版本为测试版")

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        if not self.taryShow:
            self.hide()
        else:
            if self.threadpool.activeThreadCount():
                if self._questionBox_reply():
                    a0.ignore()
                else:
                    self._thread_work_quit()
                    a0.accept()
            else:
                a0.accept()

    def _thread_work_quit(self):
        self.th_pr.stop(True)
        self.update_get.stop(True)

    def _questionBox_reply(self) -> bool:
        self.show()
        reply = QMessageBox.warning(self.centralwidget,
                                    '警告',
                                    '任务仍在进行，是否强制结束？',
                                    QMessageBox.Yes | QMessageBox.No)
        return reply != QMessageBox.Yes


if __name__ == '__main__':
    '''if 'Word2PDF.exe' in [i.name() for i in psutil.process_iter()]:
        win32api.MessageBox(win32con.NULL, 'Word2PDF已打开(>▽<)', '提醒')
    else:
        print([i.name() for i in psutil.process_iter()])'''
    app = QApplication(sys.argv)
    myWin = MainUI()
    myWin.show()
    sys.exit(app.exec_())
