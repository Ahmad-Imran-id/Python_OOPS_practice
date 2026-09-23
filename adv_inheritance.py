"""SINGLE INHERITANCE"""

class Parent_single:
    def __init__(self,name):
        self.name=name

    def intro(self):
        print(f'Hi my name is {self.name}')

class Child_single(Parent_single):
    def greet(self):
        super().intro()
        print('Hi there')
        
# obj_single=Child_single('Ahmad')
# obj_single.greet()


'''Multiple inheritance'''

class Grandparent:
    def __init__(self,name):
        self.name=name

    def intro(self):
        print(f'Hi my name is {self.name}')

class Parent(Grandparent):
    def working(self):
        print (f'{self.name} is working')

class Child(Parent):
    def playing(self):
        print (f'{self.name} is playing')

# obj_multilevel=Child('Hamza') #Child is able to use methords from both frandparent and parent
# obj_multilevel.intro()
# obj_multilevel.working()
# obj_multilevel.playing() 


'''Hirerarcle (Parent with multiple children)'''
class Parent_hire:
    def __init__(self,name):
        self.name=name

    def intro(self):
        print(f'Hi this is {self.name} and this is methrod from parent ')

class Child1_hire(Parent_hire):
    def playing(self):
        print(f'{self.name} is playing')

class Child2_hire(Parent_hire):
    def study(self):
        print(f'{self.name} is studying')

# obj_child1_hire=Child1_hire('hera') #Both child can inherit from parent but ot from eachother
# obj_child1_hire.intro()
# obj_child1_hire.playing()

# obj_child2_hire=Child2_hire('mera')
# obj_child2_hire.intro()
# obj_child2_hire.study()


'''Multiple inheritance (Diamond problem) '''

class A:
    def __init__(self,name):
        self.name=name

    def greet(self):
        print('Hi this is message from A')

class B(A):
    def greet(self):
        print('Hi this is message from B')
        super().greet()
        
class C(A):
    def greet(self):
        print('Hi this is message from C')   
        super().greet()

class D(B,C):
    def greet(self):
        print('Hi this is message from D') 
        super().greet()

#This will give greeting from all as first Ds greet is called then due to super() for B
#is called then super for C is called in that order then super from Cs greet is called 
#to call As greet methord
# obj_hire=D('not required')  
# obj_hire.greet()


'''Hybrid Inheritance'''
'''This is just multiple inheritance but the derived class explicitly calls 
constructor from one of its parent class whos constructor is dependant upon its parent
class thererfore the grandparents constructor is called and the derived class 
gets acess to all the mehtords from the grandparent class even'''

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

# Intermediate class 1 (Hierarchical)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk.")

# Intermediate class 2 (Multiple)
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

# Derived class (Multiple Inheritance)
class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name)  # Explicitly calling the constructor

    def nocturnal(self):
        print(f"{self.name} is nocturnal.")

# Create an instance of Bat
bat = Bat("Bruce")
bat.sound()     # Output: Bruce makes a sound.
bat.feed()      # Output: Bruce is feeding milk.
bat.fly()       # Output: Bruce is flying.
bat.nocturnal() # Output: Bruce is nocturnal.


        