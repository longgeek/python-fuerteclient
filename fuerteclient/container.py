#!/usr/bin/env python
# encoding: utf-8
# Author: Longgeek <longgeek@fuvism.com>

import simplejson as json

from utils import pack_requests


def create(url, username, image, cid=None):
    """ 创建容器 """

    data = {
        "action": "Container:Create",
        "params": {"username": username, "image": image, "cid": cid}
    }

    kwargs = {"url": url, "data": json.dumps(data)}
    return pack_requests(**kwargs)


def delete(url, username, cid, reset=False):
    """ 删除容器 """

    data = {
        "action": "Container:Delete",
        "params": {"username": username, "cid": cid, "reset": reset}
    }

    kwargs = {"url": url, "data": json.dumps(data)}
    return pack_requests(**kwargs)


def console(url, username, cid, cmd=None):
    """ 在容器中打入 Console 进程 """

    data = {
        "action": "Container:Console",
        "params": {"username": username, "cid": cid, "cmd": cmd}
    }

    kwargs = {"url": url, "data": json.dumps(data)}
    return pack_requests(**kwargs)


def execute(url, cid, cmds, wait=False):
    """ 在容器中执行命令 """

    data = {
        "action": "Container:Exec",
        "params": {"cid": cid, "cmds": cmds, "wait": wait}
    }

    kwargs = {"url": url, "data": json.dumps(data)}
    return pack_requests(**kwargs)
