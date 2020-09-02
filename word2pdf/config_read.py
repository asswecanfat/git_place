import configparser
from pathlib import Path


class ReadConfig(object):
    def __init__(self):
        self._config_path = 'config.ini'
        self.config = configparser.ConfigParser()
        self.config.read(self._config_path)

    def read_version(self):
        return self.config.get('version', 'version')

    def read_file_save_path(self) -> Path:  # 当前目录下的为目录非文件
        return Path.cwd() / self.config.get('savePath', 'update_file_save')

    def read_base_path(self) -> Path:
        return Path.cwd()

    def read_url(self):
        return self.config.get('BaseURL', 'url')

    def read_chiose_path(self):
        return self.config.get('LastPos', 'path')

    def change_path(self, path: Path):
        self.config.set('LastPos', 'path', str(path))
        with open(self._config_path, 'w') as f:
            self.config.write(f)

    def read_isHide(self):
        return self.config.get('haveTray', 'isHide') == str(True)

