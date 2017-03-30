#!/usr/bin/env python
# encoding: utf-8
# Author: Longgeek <longgeek@fuvism.com>

import simplejson as json
from utils import pack_requests


def create(url, username, image, cid=None, token=None):
    """创建容器

    :param str url: Fuerte api address
    :param str username: Fuvism user name
    :param str image: Image name for container
    :param str cid: The container uuid
    :param str or None token: Fuerte auth token
    """

    data = {
        "action": "Container:Create",
        "params": {"username": username, "image": image, "cid": cid}
    }
    kwargs = {"url": url, "data": json.dumps(data), "token": token}
    return pack_requests(**kwargs)


def delete(url, username, cid, reset=False, token=None):
    """删除容器

    :param str url: Fuerte api address
    :param str username: Fuvism user name
    :param str cid: The container uuid
    :param bool reset:
        reset is True, clear container data in ceph rbd
    :param str or None token: Fuerte auth token
    """

    data = {
        "action": "Container:Delete",
        "params": {"username": username, "cid": cid, "reset": reset}
    }
    kwargs = {"url": url, "data": json.dumps(data), "token": token}
    return pack_requests(**kwargs)


def console(url, username, cid, cmd=None, token=None):
    """在容器中打入 Console 进程

    :param str url: Fuerte api address
    :param str username: Fuvism user name
    :param str cid: The container uuid
    :param str or None cmd:
        str: Console command(e.g., `ipython`, `python manager.py runserver`)
        None: Bash console
    :param str or None token: Fuerte auth token
    """

    data = {
        "action": "Container:Console",
        "params": {"username": username, "cid": cid, "cmd": cmd}
    }
    kwargs = {"url": url, "data": json.dumps(data), "token": token}
    return pack_requests(**kwargs)


def execute(url, cid, cmds, wait=False, token=None):
    """在容器中执行命令

    :param str url: Fuerte api address
    :param str cid: The container uuid
    :param list cmds: List of commands to execute
    :param bool wait:
        wait is True  命令将在前台执行，会等待命令执行完成
        wait is False 命令将在后台执行，不等待命令执行完成
    :param str or None token: Fuerte auth token
    """

    data = {
        "action": "Container:Exec",
        "params": {"cid": cid, "cmds": cmds, "wait": wait}
    }
    kwargs = {"url": url, "data": json.dumps(data), "token": token}
    return pack_requests(**kwargs)
