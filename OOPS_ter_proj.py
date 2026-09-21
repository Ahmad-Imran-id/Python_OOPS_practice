class terbook:
    def __init__(self):
        self.email=''
        self.password=''
        self.signedup=False
        self.loggedin=False
        self.menu()

    def menu(self):
        menu_input=input("""
        Type 1 to signup
        Type 2 to login 
        Type 3 to write a post
        Type 4 to text your friend
        Press any button to exit""")

        if menu_input==1 or menu_input=='1' :
            self.signup()
        elif menu_input==2 or menu_input=='2':
            self.login()
        elif menu_input==3 or menu_input=='3':
            self.write_post()
        elif menu_input==4 or menu_input=='4':
            pass
        else:
            quit()


    def signup(self):
        print('You are now being signedup')
        self.email=input('\nPut in email: ')
        self.password=input('Put in password: ')
        
        if self.email !='' and self.password!='':

            self.signedup=True
            print('\nYour have been signedup')
            print(f'\nYour credentials are \n email: {self.email} \n password: {self.password}')


        else:
            print ('You are already signed in now you need to login')
            self.signup()


        self.menu()

    def login(self):
        print('You are now being loggedin')
        if self.signedup==True:
            email_check=input('Enter email: ')
            password_check=input('Enter password: ')
            if self.email==email_check and self.password==password_check:
                self.loggedin=True
                print('You are now loggedin')
            else:
                print('Your credentials are wrong try again')
                self.login()
        else:
            print('You are not signedup signup first.')

        self.menu()

    def write_post(self):
        if self.loggedin==True:
            post=input('Write your post here: ')
            print(f'The contents of your post:\n ({post})\n have been posted to your timeline')
        else:
            print('You are not loggedin login first')

        self.menu()

    

            

obj=terbook()


