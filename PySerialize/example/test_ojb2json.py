# coding=utf-8
from JsonObj.json_serialization import JSONSerialization


class expObj(JSONSerialization):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class expojb2(JSONSerialization):
    def __init__(self, name, age, expObj):
        self.name = name
        self.age = age
        self.expObj = expObj


if __name__ == '__main__':
    test = expObj("test", 100)
    print(test.to_json())

    print(test._repr__())

    test2 = expojb2("tst2", 11, test)
    print(test2.to_json())

    # print(test2._repr__())
