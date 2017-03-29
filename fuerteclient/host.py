#!/usr/bin/env python
# encoding: utf-8
# Author: Longgeek <longgeek@fuvism.com>

import simplejson as json
from utils import pack_requests


def execute(url, cmds):
    """ 在 Docker 主机上执行命 """

    data = {
        "action": "Host:Exec",
        "params": {"cmds": cmds}
    }

    kwargs = {"url": url, "data": json.dumps(data)}
    return pack_requests(**kwargs)


def read_files(url, files, cid=None):
    """ 读取 Docker 主机或容器上文件的内容 """

    data = {
        "action": "Host:ReadFiles",
        "params": {"files": files, "cid": cid}
    }

    kwargs = {"url": url, "data": json.dumps(data)}
    return pack_requests(**kwargs)


def write_files(url, files, cid=None):
    """ 为 Docker 主机或容器里写入文件内容 """

    data = {
        "action": "Host:WriteFiles",
        "params": {"files": files, "cid": cid}
    }

    kwargs = {"url": url, "data": json.dumps(data)}
    return pack_requests(**kwargs)
