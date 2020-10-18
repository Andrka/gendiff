# -*- coding:utf-8 -*-

"""Output formatters for generate differences."""

DEFAULT = 'default'
JSON = 'json'
PLAIN = 'plain'

from gendiff.format.default import default  # noqa: E402
from gendiff.format.json import json  # noqa: E402
from gendiff.format.plain import plain  # noqa: E402
