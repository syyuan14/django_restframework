""" 生成token"""
import hashlib
import datetime


def md5(password):
    """采用md5加密"""
    md = hashlib.md5()
    md.update(password.encode("utf-8"))
    c_time = str(datetime.datetime.now())
    md.update(c_time.encode("utf-8"))
    return md.hexdigest()
