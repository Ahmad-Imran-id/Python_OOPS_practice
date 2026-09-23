class Animal:
    def __init__(self,name='Generic animal'):
        self.name=name

    def speak(self):
        print(f'{self.name} makes a sound')

class Dog(Animal):
    def __init__(self, name='buddy',breed='Husky'):
        super().__init__()
        self.name=name
        self.breed=breed

    def speak(self):
        super().speak()
        print(f'{self.name} barks. Its breed is {self.breed}')


obj=Dog('honey','golden retriver')
obj.speak()

