#!/usr/bin/env python
# encoding: utf-8
# Author: Longgeek <longgeek@fuvism.com>

from _config import URL
from _config import TOKEN
from fuerteclient import container

cid = raw_input("\n检测容器是否启动，请输入容器完整 ID：")
if not cid:
    exit("\nError：未输入容器 ID.")
print "\n"
print container.is_start(
    URL,
    "longgeek",
    cid,
    TOKEN
)
