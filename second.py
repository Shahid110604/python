email="Ahmed@gmail.com"
pwd=12345
uemail=str(input("enter the email"))
upwd=int(input("enter the pwd"))
if(email == uemail):
    if(pwd ==upwd):
        print("login success")
    else:
       print("login failed due to incorrect pwd")
else:
    print("login failed due to incorrect email")