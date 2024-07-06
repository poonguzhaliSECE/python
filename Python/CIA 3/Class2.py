class info():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)
p1=info("Poojana",18)
p2=info("Poova",18)
p1.show()
p2.show()