class Parent:
    def info(self):
        print('Parent info() 호출...')

class Child(Parent):
    pass

p = Parent()
p = Child()
p.info()