# -*- coding: utf-8 -*-

from hagworm.extend.metaclass import Singleton


class Apoll(Singleton):

    def __init__(self):
        self.data = {}

    def set(self, data):
        self.data = data

    def get(self):
        return self.data

    def delete(self):
        pass

    def update(self):
        pass
