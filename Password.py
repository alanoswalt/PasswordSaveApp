#Class that has the attributes of the account.
class account():
    def __init__(self, name, email_username, password):
        self.name = name
        self.email_username = email_username
        self.password = password
    def __str__(self):
        #return "This is the info of a " + self.name + " with the user " +self.email_username +" and password "+ self.password
        return "This is the info of a {} with the user {} and password {}".format(self.name, self.email_username, self.password)



def create(name, email, password):
    new_account = account(name, email, password)
    print(new_account)
    return None

def main():
    x = input('Dame el tipo de cuenta (Gmail, Outlook, Netflix): ')
    y = input('Dame el correo o usuario: ')
    z = input('Dame la contraseña: ')
    create(x, y, z)

if __name__=="__main__":
    main()
