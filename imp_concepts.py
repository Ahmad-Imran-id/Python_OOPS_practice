class Encapsulation:
    __id=0
    def __init__(self):
        Encapsulation.__id+=1
        self.__name='Default name'

    def setter_name(self,value): #setter for hidden attribute name
        self.__name=value
    
    def getter_name(self): #getter for hidden attribute name
        return self.__name

    @staticmethod
    def setter_id(val): 
        Encapsulation.__id=val

    @staticmethod
    def getter_id():
        return Encapsulation.__id

    def give_info(self):
        print(f'Name: {self.getter_name()}, id: {self.getter_id()}')
    
