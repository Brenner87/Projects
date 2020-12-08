import builtins
from collections import *

c = ChainMap()        # Create root context
d = c.new_child()     # Create nested child context
print (c)
print (d)
e = c.new_child()     # Child of c, independent from d
print(e.maps[0])             # Current context dictionary -- like Python's locals()
print(e.maps[-1])            # Root context -- like Python's globals()
print(e.parents)             # Enclosing context chain -- like Python's nonlocals

#print(d['x'])                # Get first key in the chain of contexts
d['x'] = 1              # Set value in current context
c['y'] = 1
print (d)
print (d.maps[1])
print (e)


Point = namedtuple('Point', ['x', 'y'])

#p = Point(11, y= 22)
#print (p)

t = [11, 22]
print(Point._make(t))

#del d['x']            # Delete from current context
#items(d)               # All nested values
#k in d                # Check all nested values
#len(d)                # Number of nested values
#d.items()             # All nested items
#dict(d)               # Flatten into a regular dictionary
