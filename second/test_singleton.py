# -*-coding:utf8-*-

print('&&&&')
from singleton_object import SingletonObject
print('&&&&&')

print('begin obj1:')
obj1 = SingletonObject()
obj1.val = "Object Value 1"
print('*****obj1*****')
print(obj1)

print('++++++++++++++')
obj2 = SingletonObject()
# print(SingletonObject.instance)
# print(obj2)
# obj2.val = "Object Value 2"
# print('*****obj1*****')
# print(obj1)
# print('*****obj2*****')
# print(obj2)









