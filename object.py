
# actual creation of an object
class fan():
    def __init__(self):
        self.color='black'
        self.cost=1500
        self.brand='bajaj'
        self.noofblades=4
        print(self)
f1=fan()
print(f1)
f2=f1
print(f2)
print(id(f1))
print(id(f2))
print(f1 is f2)