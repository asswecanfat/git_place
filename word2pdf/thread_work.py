from PyQt5.QtCore import QRunnable, pyqtSlot
from pathlib import Path
from qt_signal import QTSignal
from w2f import word_2_pdf
from update import get_update_url_path_sizeUrl, check_update
import requests
from subprocess import Popen  # 非阻塞
from loguru import logger


class FileThread(QRunnable):

    def __init__(self, file_list: list = None):
        super(FileThread, self).__init__()
        self.file_list = file_list
        self.text_signal = QTSignal()
        self._stop = False

    def update_file_list(self, file_list: list):
        self.file_list = file_list

    def stop(self, b: bool = False):
        self._stop = b

    @pyqtSlot()
    def run(self) -> None:
        self.text_signal.changeIcon.emit(True)  # 确认开启
        if files_num := len(self.file_list):
            self.text_signal.text_edit.emit(f'---开始转换{files_num}个文档文件！\n')
        for num, file_name in enumerate(self.file_list):
            file_ca = Path(file_name)
            if self._stop:
                break
            if word_2_pdf(file_ca, file_ca.parent / f'{file_ca.stem}.pdf'):
                self.text_signal.text_edit.emit(f'{file_name}转换完成！({num + 1}/{files_num})\n')
            else:
                self.text_signal.text_edit.emit(f'{file_name}转换失败！({num + 1}/{files_num})\n')
        self.text_signal.complete.emit(True)
        self.text_signal.changeIcon.emit(False)


class UpdateCheck(QRunnable):
    def __init__(self, verSion: float):
        super(UpdateCheck, self).__init__()
        self.verSion = verSion
        self.signal = QTSignal()

    @pyqtSlot()
    def run(self) -> None:
        self.signal.haveUpdate.emit(check_update(self.verSion))


class UpdateGet(QRunnable):
    def __init__(self):
        super(UpdateGet, self).__init__()
        self.signal = QTSignal()
        self._stop = False

    def stop(self, b: bool = False):
        self._stop = b

    def run(self) -> None:
        self.signal.downing.emit(True, 0)
        url, save_path, size_url = get_update_url_path_sizeUrl()
        try:
            with open(save_path, 'wb') as f:
                res = requests.get(url, stream=True)
                # 写入文件
                offset = 0
                file_size = requests.get(size_url).json()['size']
                for chunk in res.iter_content(chunk_size=10240):
                    if not chunk and not self._stop:
                        break
                    f.seek(offset)
                    f.write(chunk)
                    offset += len(chunk)
                    self.signal.downing.emit(True, round(offset / int(file_size) * 100, 2))
                self.signal.downing.emit(False, 0)
        except Exception as e:
            logger.info(e)
            self.signal.downing.emit(False, 0)
        else:
            self.signal.sureDown.emit(True)


class UpdateInstall(QRunnable):
    def __init__(self):
        super(UpdateInstall, self).__init__()

    def run(self) -> None:
        Popen('updateBot.exe')
