#!/usr/bin/python3

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            return {k: v for k, v in self.__dict__.items() if k in attrs and type(k) is str}
        return self.__dict__
