# -*-coding:utf8-*-


class Foo:
    name = "Foo"
    @property
    def AAA(self):
        print('get的时候运行我啊')

    @AAA.setter
    def AAA(self,value):
        print('set的时候运行我啊',value)

    @AAA.deleter
    def AAA(self):
        del Foo.name
        print('delete的时候运行我啊')

#只有在属性AAA定义property后才能定义AAA.setter,AAA.deleter
f1=Foo()

f1.AAA
#setter
f1.AAA='aaa'
print(Foo.name)
#deleter
del f1.AAA
#删除完毕后,再次调用报如下错误
#AttributeError: type object 'Foo' has no attribute 'name'
print(Foo.name)







