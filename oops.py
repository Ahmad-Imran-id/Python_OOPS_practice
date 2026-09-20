class Employee:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id

    def travel(self,destination):
        print(f'Employee plans to travel to {destination}')

    def employee_information(self,destination):
        print(f'Name:{self.name}\n age:{self.age} \n id:{self.id}')
        self.travel(destination)


Employee_1=Employee('Ahmad',21,1)

Employee_1.employee_information('Moroco')
