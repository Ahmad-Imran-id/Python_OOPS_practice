'''THis is a demo project ment to somewhat replicate the functionality of
facebook inside terminal. This has no real usecase it was done just to create a demo
project using OOPS'''


class terbook:
    #Constructor with all the required variables:
    def __init__(self): 
        self.email=''
        self.password=''
        self.signedup=False
        self.loggedin=False
        self.login_tries=0
        self.menu()

    #Main menu to select what you want to do:
    def menu(self): 
        self.login_tries=0 
        menu_input=input("""
        Type 1 to signup
        Type 2 to login 
        Type 3 to write a post
        Type 4 to text your friend
        Press any button to exit: """)

        if str(menu_input)=='1':
            self.signup()
        elif str(menu_input)=='2':
            self.login()
        elif str(menu_input)=='3':
            self.write_post()
        elif str(menu_input)=='4':
            self.text_friend()
        else:
            quit()


    #Methord to signup:
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


    #Methord to login, requires user to be signedup first, 
    #boots back to menu if tried exceed 3
    def login(self): 
        
        
        if self.login_tries<3:
            if self.signedup==True:
                print('You are now being loggedin')
                self.login_tries+=1
                email_check=input('Enter email: ')
                password_check=input('Enter password: ')

                if self.email==email_check and self.password==password_check:
                    self.loggedin=True
                    print('You are now loggedin')

                else:
                    print(f'''Your login credentials are wrong. You have {3-self.login_tries} 
                          remaining ''')
                    self.login()

            else:
                print('You are not signedup signup first.')

        else:
            print('Login tries exeded you booting menu again')

        self.menu()

    #Methord to write post,requires user to be loggedin first:
    def write_post(self): 
        if self.loggedin==True:
            post=input('Write your post here: ')
            print(f'The contents of your post:\n ({post})\n have been posted to your timeline')

        else:
            print('You are not loggedin login first')

        self.menu()


    #Methord to text someone, requires user to be loggedin:
    def text_friend(self):
        if self.loggedin==True:
            friend=input('Who do you want to send this text to: ')
            text=input(f'Write what you want to send to {friend}: ')
            print(f'The contents of you message \n ({text})\n have been sent to ({friend})')

        else:
            print('You are not logged in login first')

        self.menu()

   
obj=terbook()


