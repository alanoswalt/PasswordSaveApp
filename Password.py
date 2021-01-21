#Class that has the attributes of the account.
import sqlite3

class account():
    def __init__(self, name, email_username, password):
        self.name = name
        self.email_username = email_username
        self.password = password
    def __str__(self):
        #return "This is the info of a " + self.name + " with the user " +self.email_username +" and password "+ self.password
        return "This is the info of a {} with the user {} and password {}".format(self.name, self.email_username, self.password)



def load_file(new_account):
    conn = sqlite3.connect('accountsdb.sqlite')
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Accounts (
        type   TEXT,
        mail_user   TEXT,
        password TEXT
    )''')

    cur.execute('''INSERT OR IGNORE INTO Accounts (type)
        VALUES ( ? )''', ( new_account.name, ) )

    cur.execute('''INSERT OR IGNORE INTO Accounts (mail_user)
        VALUES ( ? )''', ( new_account.email_username, ) )

    cur.execute('''INSERT OR IGNORE INTO Accounts (password)
        VALUES ( ? )''', ( new_account.password, ) )
    cur.close()
    conn.commit()
    return None

def create(name, email, password):
    new_account = account(name, email, password)
    print(new_account)
    return new_account

def main():
    x = input('Dame el tipo de cuenta (Gmail, Outlook, Netflix): ')
    y = input('Dame el correo o usuario: ')
    z = input('Dame la contraseña: ')
    account = create(x, y, z)
    load_file(account)


if __name__=="__main__":
    main()
