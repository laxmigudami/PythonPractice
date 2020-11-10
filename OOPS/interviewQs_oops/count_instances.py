# How to get the count of number of instances of a class that is being created.
class Login:
    login_count = 0 #class variable that keeps count of login counts
    def __init__(self):
        Login.login_count += 1

u1 = Login()
print(Login.login_count)

u2 = Login()
print(Login.login_count)
