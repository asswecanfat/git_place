import hashlib
from datetime import datetime


def deal_hash(path: str):
    to_md5 = hashlib.md5(path.encode('utf-8'))
    return to_md5.hexdigest()


def get_time(end_time):
    return str((end_time - datetime.now()).total_seconds())
