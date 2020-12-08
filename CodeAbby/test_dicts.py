dic={}
keys=['one','two', 'three']
value='numbers'

def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value


def nested_get(dic, keys):
    items=dic
    for key in keys:
        items = items.get(key)
    return items


nested_set(dic, keys, value)

print (dic)

print(nested_get(dic, keys))