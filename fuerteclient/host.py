#!/usr/bin/env python
# encoding: utf-8
# Author: Longgeek <longgeek@fuvism.com>

import simplejson as json
from utils import pack_requests


def execute(url, cid, cmds, token=None):
    """在容器所在 Docker 主机上执行命令

    :param str url: Fuerte api address
    :param str cid: The container uuid
    :param list cmds: List of commands to execute
    :param str or None token: Fuerte auth token
    """

    data = {
        "action": "Host:Exec",
        "params": {"cid": cid, "cmds": cmds}
    }
    kwargs = {"url": url, "data": json.dumps(data), "token": token}
    return pack_requests(**kwargs)


def read_files(url, files, cid=None, token=None):
    """在 Docker 主机或容器中读取文件内容

    :param str url: Fuerte api address
    :param dict files:
        e.g.: {"/etc/hosts": "",
               "/tmp/test.txt": "the test.txt default content."}
    :param str or None cid: The container uuid
        cid is str: 读取容器里的文件内容
        cid is None: 读取主机里的文件内容
    :param str or None token: Fuerte auth token
    """

    data = {
        "action": "Host:ReadFiles",
        "params": {"files": files, "cid": cid}
    }
    kwargs = {"url": url, "data": json.dumps(data), "token": token}
    return pack_requests(**kwargs)


def write_files(url, files, cid=None, token=None):
    """为 Docker 主机或容器里写入文件内容

    :param str url: Fuerte api address
    :param dict files:
        e.g.: {"/etc/hosts": "",
               "/tmp/test.txt": "the test.txt default content."}
    :param str or None cid: The container uuid
        cid is str: 为容器里的文件写入内容
        cid is None: 为当前主机的文件写入内容
    :param str or None token: Fuerte auth token
    """

    data = {
        "action": "Host:WriteFiles",
        "params": {"files": files, "cid": cid}
    }
    kwargs = {"url": url, "data": json.dumps(data), "token": token}
    return pack_requests(**kwargs)


def fd_check(url, cid, fds, token=None):
    """在容器所在 Docker 主机上检测文件、目录是否创建

    :param str url: Fuerte api address
    :param str cid: The container uuid
    :param list fds: 要检测的数据结构
        e.g.: [
            {"type": "dir", "name": "/some/dirname"},
            {"type": "file", "name": "/some/filename"}
        ]
    :param str or None token: Fuerte auth token
    """

    data = {
        "action": "Host:FdCheck",
        "params": {"cid": cid, "fds": fds}
    }
    kwargs = {"url": url, "data": json.dumps(data), "token": token}
    return pack_requests(**kwargs)
