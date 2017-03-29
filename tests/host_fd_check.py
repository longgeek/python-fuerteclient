#!/usr/bin/env python
# encoding: utf-8
# Author: Longgeek <longgeek@fuvism.com>

from api_url import URL
from fuerteclient import host

cid = raw_input(
    "\n在容器所在 Docker 主机上检测文件、目录是否创，\
\n请输入容器完整 ID："
)
if not cid:
    exit("\nError：未输入容器 ID.")
print "\n"
print host.fd_check(
    URL,
    cid,
    [
        {"type": "dir", "name": "/etc/hostss"},
        {"type": "file", "name": "/etc/hosts"}
    ]
)
