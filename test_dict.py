import yaml
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car = car.setdefault("model", "Bronco")


a={'a':{'k':['f', 'b', 'c'],'1':'e'}, 'b':{'z':{'f':3}}}

b={'a': {'k':['f', 'b', 'c']}}
print(b.items() <= a.items())

#print({'a':{'k':['f', 'b', 'c']}} in a)

a='1'
print(float(a))