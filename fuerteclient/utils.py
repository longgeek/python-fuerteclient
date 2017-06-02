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

    kwargs["headers"] = {"content-type": "application/json"}
    if kwargs["token"]:
        kwargs["headers"]["token"] = "Bearer %s" % kwargs["token"]
    kwargs.pop("token")
    try:
        req = requests.post(**kwargs)
    except Exception, e:
        return (-1, str(e), "")
    status = req.status_code
    data = req.json()
    if status != 200:
        inner_code = data.get('inner_code')
        if inner_code:
            return (inner_code, data.get("error"), "")
        else:
            return (status, req.text, "")
    return (0, data.get("message"), data.get("data"))
