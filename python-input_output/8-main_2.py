MyClass = __import__('8-my_class_2').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.win()

mj = class_to_json(m)
print(mj)
# {'number': 4, '_MyClass__name': 'John', 'is_team_red': True, 'score': 1}
