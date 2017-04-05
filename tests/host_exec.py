#!/usr/bin/env python
# encoding: utf-8
# Author: Longgeek <longgeek@fuvism.com>

from api_url import URL
from fuerteclient import host

cid = raw_input("\n在容器所在 Docker 主机上执行命令，请输入容器完整 ID：")
if not cid:
    exit("\nError：未输入容器 ID.")
print "\n"
print host.execute(
    URL,
    cid,
    "longgeek",
    ["mkdir /tmp/dir1", "mkdir /tmp/dir2"]
)
