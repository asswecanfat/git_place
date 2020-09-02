import requests
import psutil
import shutil
from config_read import ReadConfig
from loguru import logger
import os

congfig = ReadConfig()


def check_update(version: float) -> bool:
    url = f'{congfig.read_url()}checkVersion/{version}'
    try:
        res = requests.get(url)
        return res.json()['state']
    except Exception as e:
        logger.info(e)
        return False


@logger.catch
def get_update_url_path_sizeUrl() -> (str, str, str):
    down_url = f'{congfig.read_url()}download'
    size_url = f'{congfig.read_url()}size'
    return down_url, str(congfig.read_file_save_path() / 'cache.zip'), size_url


@logger.catch
def install_update() -> None:
    for proc in psutil.process_iter():
        if proc.name() == 'Word2PDF.exe':
            proc.kill()
            break
    cache_file = congfig.read_file_save_path() / 'cache.zip'
    shutil.unpack_archive(filename=str(cache_file),
                          extract_dir=str(congfig.read_base_path()))
    cache_file.unlink()
    os.system('echo 更新成功！&& pause')  # 按任意键继续


if __name__ == '__main__':
    print(check_update(1.6))
