#fucking decorators

def check_login(login):
    def islogin(username):
        checklogin = True
        if not checklogin:
            print("not logged in ");
            login(username)
        else:
            print("user already logged in ")
    return islogin

@check_login
def login(username):
    print(username, "logged in successully")

login("Dnyaneshwar")



