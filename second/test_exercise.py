# -*-coding:utf8-*-

from exercise import SingletonObject

log_object1 = SingletonObject()
log_object1.file_name = 'logfile/log_exercise.log'
print(log_object1.file_name)
log_object1.critical('This is a critical message from object1')


log_object2 = SingletonObject()
print(log_object2.file_name)
log_object2.error('This is a error message from object2')







