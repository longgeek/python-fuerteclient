#!/usr/bin/env python
# encoding: utf-8
# Author: Longgeek <longgeek@fuvism.com>

from _config import URL
from _config import TOKEN
from fuerteclient import container


print container.create(
    URL,
    "longgeek",
    "192.168.80.117:5000/longgeek/ubuntu-14.04.1:base",
    None,
    TOKEN
)
