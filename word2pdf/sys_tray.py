from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtWidgets import QSystemTrayIcon, QAction, QMenu


class AppTray(QSystemTrayIcon):
    def __init__(self, mainWin):
        self.mw = mainWin
        super(AppTray, self).__init__(self.mw)
        self.base_icon = QIcon(r'static\pic\main_ui.ico')
        self.setIcon(self.base_icon)
        self.trayMenu = QMenu(self.mw)
        self.init_menu_func()
        self.setContextMenu(self.trayMenu)
        self.activated.connect(self.icon_doubule_click)
        self.setToolTip('ο(=•ω＜=)ρ⌒☆测试版哦')
        self.show()

    def _exit(self):  # 可选用方法
        # QCoreApplication 包含主事件循环；它处理和调度所有事件。instance()方法为我们提供了其当前实例
        if self.mw.threadpool.activeThreadCount():
            if not self.mw._questionBox_reply():
                self.mw._thread_work_quit()
                QCoreApplication.instance().quit()
        else:
            QCoreApplication.instance().quit()

    def init_menu_func(self):
        icon = QIcon()
        icon.addPixmap(QtGui.QPixmap("static/pic/quit.pbm"), QIcon.Normal, QIcon.Off)
        quitAction = QAction('退出', self.mw)  #
        quitAction.setIcon(icon)
        quitAction.triggered.connect(self._exit)
        self.trayMenu.addAction(quitAction)

    def icon_doubule_click(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.mw.show()

    def dealFile_set_icon(self, b):
        if b:
            gif_icon = QMovie(r'static\pic\download.gif')
            gif_icon.frameChanged.connect(lambda: self.setIcon(QIcon(gif_icon.currentPixmap())))
            gif_icon.start()
        else:
            self.setIcon(self.base_icon)
