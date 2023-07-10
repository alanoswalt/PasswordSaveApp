import re
import operator
import csv

def retrive_logs():
    f = []
    error = {}
    users = {}
    with open('logs.log','r') as file:
        f = file.readlines()

    for log in f:
        type=re.search(': ([A-Z]*)',log)
        name = re.search(r'\(([a-z.]*)\)', log) #to catch the element use parenteis to print them use [1]
        if type[1]=='INFO':
            if name[1] in users:
                users[name[1]]['INFO'] += 1
            else:
                users[name[1]] = {'INFO': 1, 'ERROR': 0}
            #print(users)

        elif type[1] == 'ERROR':
            err = re.search('ERROR ([A-Za-z \']*) \(', log)
            if err[1] in error:
                error[err[1]] += 1
            else:
                error[err[1]] = 1

            if name[1] in users:
                users[name[1]]['ERROR'] += 1
            else:
                users[name[1]] = {'INFO': 0, 'ERROR': 1}
            #print(error)
    return (users, error)


def arrange_logs(users, error):
    error = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
    users = sorted(users.items())
    print(error)
    print(users)
    return(users, error)

def write_logs(users,error):
    with open('error_message.csv', 'a+', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(["Error","Count"])
        for err, amount in error:
            writer.writerow([err,amount])

    with open('user_statistics.csv', 'a+', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(["Username", "INFO", "ERROR"])
        for user, info_errors in users:
            writer.writerow([user,info_errors['INFO'],info_errors['ERROR']])

def main():
    users, error = retrive_logs()
    users, error = arrange_logs(users, error)
    write_logs(users,error)

if __name__=="__main__":
    main()
./csv_to_html.py error_message.csv /var/www/html/error_table.html
./csv_to_html.py user_statistics.csv /var/www/html/user_table.html
