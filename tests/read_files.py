#!/usr/bin/env python
# encoding: utf-8
# Author: Longgeek <longgeek@fuvism.com>

from _config import URL
from _config import TOKEN
from fuerteclient import host

cid = raw_input("\n如需要为容器里的文件写入内容，需要输入容器完整的 ID,\
                 \n或\n如需要在 Docker 主机里读取文件内容，请直接按回车：")
if not cid:
    cid = None
files = {"/etc/hosts": "", "/tmp/test.txt": "test.txt the content."}
print "\n"
print host.read_files(
    URL,
    files,
    cid,
    TOKEN
)
