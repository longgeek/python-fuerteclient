#!/usr/bin/env python
# encoding: utf-8
# Author: Longgeek <longgeek@fuvism.com>

from _config import URL
from _config import TOKEN
from fuerteclient import container

cid = raw_input("\n删除容器操作，请输入容器完整 ID：")
if not cid:
    exit("\nError：未输入容器 ID.")
print "\n"
print container.delete(
    URL,
    "longgeek",
    cid,
    False,
    TOKEN
)
