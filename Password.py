

#Class that has the attributes of the account.
class account():
    def __init__(self, name, email_username, password):
        self.name = name
        self.email_username = email_username
        self.password = password
    def __str__(self):
        return "This is the info of a " + self.name

correo = account("Outlook", "alan@outlook.com", "pepeeltoro")

print(correo)
