class terbook:
    def __init__(self):
        self.email=''
        self.password=''
        self.signedin=False
        self.menu()

    def menu(self):
        menu_input=input("""
        Type 1 to signup
        Type 2 to signin 
        Type 3 to write a post
        Type 4 to text your friend
        Press any button to exit""")

        if menu_input==1 or menu_input=='1' :
            self.signup()
        elif menu_input==2 or menu_input=='2':
            pass
        elif menu_input==3 or menu_input=='3':
            pass
        elif menu_input==4 or menu_input=='4':
            pass
        else:
            quit()


    def signup(self):
        self.email=input('\nPut in email: ')
        self.password=input('Put in password: ')
        print(f'\nYour credentials are \n email: {self.email} \n password: {self.password}')
        print('\nYour have been signedup')


obj=terbook()


