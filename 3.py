# # for loop
# str="ramya"
# for i in str:
#     print(i,end="")
# print(i)
# print(i)

# # for range  (stop)
# for i in range(10):
#     print("hello word")
# print(i)

# for i in range(6):
#     print("hello word")
# print(i)


# class fan:
#     def __init__(self):
#         self.color="black"
#         self.cost=1500
#         self.brand="bajaj"
#         self.noofblades=4
#     def rotate(self):
#         print("fan is rotataing")
#     def on(self):
#         print("fan is on")

# f1=fan()
# print(f1.color)
# print(f1.cost)
# print(f1.brand)


# class hero:
#     def __init__(self):
#         self.name="kholi"
#         self.age=45
#         self.passion="crictek"
#     def passion(self):
#         print(" He is best criketer")
#     def actor(self):
#         print("He is the gud actor and singer")

# f2=hero()
# print(f2.name)
# print(f2.age)

# f2.age= 42
# print (f2.age)
# f2.name="rahul"
# print(f2.name)

class hero:
    def __init__(self):
        self.name="yash"
        self.age=44
        self.weight=78
    def dance(self):
        print("hero is dancing")

h1=hero()
print(h1.name)
h2=h1
print(h1)
print(h2)
print(h2.age)
print(id(h1))
print(h1 is h2)