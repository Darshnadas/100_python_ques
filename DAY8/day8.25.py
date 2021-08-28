"""
Define a class, which have a class parameter and have a same instance parameter.
"""
class Water:
    name = "Water"

    def __init__(self, name = None):
        self.name = name 

fish = Water("whale")
print("%s name is %s"%(Water.name, fish.name))

shark = Water()
shark.name = "dolphine"
print("%s name is %s"%(Water.name, shark.name))
