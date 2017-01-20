# coding=utf-8
import json
from argparse import Namespace
from collections import namedtuple


class JsonDeserialization(object):
    @staticmethod
    def json2obj(json_data):
        return json.loads(json_data, object_hook=lambda d: Namespace(**d))

    def _json_object_hook(d):
        return namedtuple('x_obj', d.keys())(*d.values())

    @staticmethod
    def json2obj_base(data):
        return json.loads(data, object_hook=JsonDeserialization._json_object_hook)
