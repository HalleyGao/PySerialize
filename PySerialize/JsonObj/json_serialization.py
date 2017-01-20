# coding=utf-8
import json


class JSONSerialization(object):
    #
    def __repr__(self):
        return json.dumps(self.__dict__)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
