# -*-coding:utf8-*-

class SingletonObject(object):
    class __SingletonObject():
        def __init__(self):
            self.file_name = None

        def _write_log(self, level, msg):
            with open(self.file_name, 'a') as file_log:
                file_log.write('[{0}] {1}\n'.format(level, msg))

        def critical(self, msg):
            self._write_log('CRITICAL', msg)

        def error(self, msg):
            self._write_log('ERROR', msg)

    instance = None

    def __new__(cls):
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject.__SingletonObject()
        return SingletonObject.instance
