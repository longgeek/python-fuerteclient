#!/usr/bin/env python
# encoding: utf-8
# Author: Longgeek <longgeek@fuvism.com>

from api_url import URL
from fuerteclient import host

cid = raw_input("\n如需要为容器里的文件写入内容，需要输入容器完整的 ID，\
                 \n或\n如需要在 Docker 主机里上写入文件内容，请直接按回车：")
if not cid:
    cid = None
files = {
    "/tmp/test1.txt": "test1.txt the content.",
    "/tmp/test2.txt": "test2.txt the content."
}
print "\n"
print host.write_files(
    URL,
    files,
    cid
)
