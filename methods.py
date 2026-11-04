# case1
class calculator:
    def __init__(self):
        self.x=10
    def add(self):
        a=10
        b=20
        c=a+b
        print(c)
c1=calculator()
print(c1.x)
c1.add()

# case2    
class calculator:
    def __init__(self):
        self.x=10
    def add(self):
        a=10
        b=20
        c=a+b
        return c
c1=calculator()
print(c1.x)
r1=c1.add()
print(r1)

# case3
class calculator:
    def __init__(self):
        self.x=10
    def add(self, a,b):
        c=a+b
        print(c)
c1=calculator()
print(c1.x)
# step1
c1.add(10,20) 

         # or
n1=10
n2=30
c1.add(n1,n2)

# case4
class calculator:
    def __init__(self):
        self.x=10
    def add(self , a,b):
        c=a+b
        return c
c1=calculator()
print(c1.x)
r1=c1.add( 50,20)
print(r1)
    # or
c1=calculator()
n1=20
n2=20
r1=c1.add(n1,n2)
print(r1)