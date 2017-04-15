#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Longgeek <longgeek@fuvism.com>

import requests

from requests.packages.urllib3.exceptions import SNIMissingWarning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.packages.urllib3.exceptions import InsecurePlatformWarning


# Disable requests the warnings
requests.packages.urllib3.disable_warnings(SNIMissingWarning)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)


def pack_requests(**kwargs):
    """Add a certificate for requests

    :returns: (
        status: int
        message: str
        result: dict
    )
    """

    try:
        kwargs["headers"] = {"content-type": "application/json"}
        if kwargs["token"]:
            kwargs["headers"]["token"] = "Bearer %s" % kwargs["token"]
        kwargs.pop("token")
        req = requests.post(**kwargs)
        status = req.status_code
        if status != 200:
            try:
                return (req.json()["inner_code"], req.json()["error"], "")
            except Exception, e:
                return (status, req.text, "")
        return (0, req.json()["message"], req.json()["data"])
    except Exception, e:
        return (-1, e, "")
