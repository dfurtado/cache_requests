#!/usr/bin/env python
# coding=utf-8
"""
==============
cache_requests
==============

**Simple. Powerful. Persistent LRU caching for the requests library.**

.. topic:: ELI5

    **If you call the same function with the same parameters TWO times, it only does
    the work ONE time.**  Results from the function are cached in storage and retrieved
    from storage.

    It gets worse.  Unlike a regular LRU cache, the results are not destroyed when the
    program finishes. Instead its destroyed when it expires.

"""
from __future__ import absolute_import

import logging

from .cache_requests import redis_memoize, RedisMemoize, Config
from .patch import patch_requests, unpatch_requests

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:  # pragma: no cover
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())

__author__ = 'Manu Phatak'
__email__ = 'bionikspoon@gmail.com'
__version__ = '1.0.0'
__all__ = ['redis_memoize', 'RedisMemoize', 'Config', 'patch_requests', 'unpatch_requests']
