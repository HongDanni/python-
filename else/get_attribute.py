# -*-coding:utf8-*-


class Tree(object):
    def __init__(self, name):
        self.name = name
        self.cate = "plant"

    def __getattribute__(self, obj):
        print("哈哈")
        return object.__getattribute__(self, obj)

    
aa = Tree("大树")
print(aa.name)


