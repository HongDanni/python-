# -*-coding:utf8-*-


class Tree(object):
    def __init__(self, name):
        self.name = name
        self.cate = "plant"

    def __getattribute__(self, obj):
        print("哈哈")
        print(object.__getattribute__(self, 'cate'))
        print(object.__getattribute__(self, obj))
        return object.__getattribute__(self, obj)


aa = Tree("大树")
# aa.name
print(aa.name)
# print(aa.name)


