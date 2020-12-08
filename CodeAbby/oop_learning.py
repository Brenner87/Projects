def main():
    friends = []
    running = True
    while running:
        print ("\nContacts manager")
        print ("1) new contact     2) lookup")
        print ("3) show all        4) end")
        option = input("> ")
        if option == '1':
            friends.append(enter_a_friend())
        elif option == '2':
            lookup_a_friend(friends)
        elif option =='3':
            show_all_friends(friends)
        elif option =='4':
            running = False
        else:
            print ("Unrecognised input, please try again.")
    print ("Program ending")



class Person(object):

    #constructor
    def __init__(self, theName, thePhone, theEmail):
        self.name=theName
        self.phone=thePhone
        self.email=theEmail

    # Accessor methods(accessors)

    def getName(self):
        return self.name

    def getPhone(self):
        return self.phone

    def getEmail(self):
        return self.email


    #Mutator methods(mutators)

    def setName(self, newName):
        self.name = newName

    def setPhone(self, newPhone):
        self.phone = newPhone

    def setEmail(self, newEmail):
        self.email = newEmail

    def __str__(self):
        return "Person[ name = " + self.name + \
                ", phone = " + self.phone + \
                ", email = " + self.email + \
                " ]"

def enter_a_friend():
    name = input("Enter friend's name: ")
    phone = input("Enter friend's Phone: ")
    email = input("Enter friend's Email: ")
    return Person(name, phone, email)

def lookup_a_friend(friends):
    found = False
    name = input("Enter name to lookup: ")
    for friend in friends:
        if name in friend.getName():
            print ( friend )
            found = True
        if not found: print("No friends match the term")

def show_all_friends(friends):
    print("Showing all contacts:")
    for friend in friends:
        print ( friend )




if __name__=="__main__":
    main()