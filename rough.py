# from oops import Employee

# e1=Employee('jid',32,1)
# #print(e1.__test) this will not run
# print(e1._Employee__test) #This will run as python cannot protect attributes it can only hide them

from imp_concepts import Encapsulation

obj_en=Encapsulation()
obj_en.setter_name('Ahmad')
obj_en.give_info()

obj2=Encapsulation()

obj2.give_info()