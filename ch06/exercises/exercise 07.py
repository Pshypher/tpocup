# Program displays a menu, and asks the user for a choice

def display_menu():
    menu_str = "1. Messaging\n2. Contacts\n3. Games\n4. Settings\n5. Media\
                \n6. Web\n: "
    valid = False
    
    while not valid:
        try:
            choice_str = input("Select one of the options below:\n{:s}".format(menu_str))
            choice_int = int(choice_str)
            if choice_int >= 1 and choice_int <= 6:
                if choice_int == 1:
                    compose_message()
                elif choice_int == 2:
                    search_contacts()
                elif choice_int == 3:
                    play_games()
                elif choice_int == 4:
                    change_settings()
                elif choice_int == 5:
                    media()
                else:
                    surf_web()
                valid = True
            else:
                print("Selected option should be numbers between 1-6")
        except ValueError:
            print("Only Digits are allowed")
            print("Numbers between 1-6")
            
def compose_message():
    pass

def search_contacts():
    pass

def play_games():
    pass

def change_settings():
    pass

def media():
    pass

def surf_web():
    pass


            