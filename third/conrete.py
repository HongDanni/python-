# -*-coding:utf8-*-

from prototype_1 import Prototype
from copy import deepcopy

class Concrete(Prototype):
    def clone(self):
        return deepcopy(self)





