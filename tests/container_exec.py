#!/usr/bin/env python
# encoding: utf-8
# Author: Longgeek <longgeek@fuvism.com>

from api_url import URL
from fuerteclient import container

cid = raw_input("\n在容器中执行命令，请输入容器完整 ID：")
if not cid:
    exit("\nError：未输入容器 ID.")
print "\n"
print container.execute(
    URL,
    cid,
    ["cat /etc/hosts"]
)
