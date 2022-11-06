objects = [[] for i in range(2)]

def add_object(o, depth):
    objects[depth].append(o)

def add_objects(ol, depth):
    objects[depth] += ol

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            del o
            return
    raise ValueError('Trying destroy non existing object')

def all_object():
    for layer in objects:
        for o in layer:
            yield o

def clear():
    for o in all_object():
        del o
    for layer in objects:
        layer.clear()