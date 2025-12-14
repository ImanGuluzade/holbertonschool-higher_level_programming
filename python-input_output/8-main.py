MyClass = __import__('8-my_class').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.number = 89

mj = class_to_json(m)
print(type(mj))  # <class 'dict'>
print(mj)        # {'name': 'John', 'number': 89}
