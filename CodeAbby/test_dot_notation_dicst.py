from types import SimpleNamespace
import yaml


a = SimpleNamespace()

a.one = SimpleNamespace()
a.one.two = '2'

print(a.__dict__)
print(yaml.dump(a.__dict__))

# b = {'one': 1, 'two': 2}
# print(b.__dict__)
# print(getattr(b, '__dict__'))