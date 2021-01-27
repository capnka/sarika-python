print ("Hi user, welcome to Secret Saver.")
enter_username = input ("What would you like your username to be?  \n >>>")
enter_password = input ("And your password? : \n >>>")
enter_secret = input ("What is the secret you would like to save?  \n >>>")
print ("Thank You for sharing, your secret is safe with us.\n \n")
print()
input("Press ENTER to continue...")
enter_yesorno = input ("Would you like to see the secret? (case sensitive yes or no question)  \n >>>")
if enter_yesorno == "yes" :
    saved_username = input ("What is your username?  \n >>>")
    if saved_username == enter_username :
        saved_password = input ("Hello, "+enter_username+" what is your password?  \n >>>")
        if saved_password == enter_password:
           print ("The secret saved by this account is '"+enter_secret+"'")
        else :
             print ("Wrong password.")
    else :
        print ("We have not met someone with this username.")

elif enter_yesorno == "no" :
    print ("Alright,the secret is safe with us." )
else:
    print ("We do not identify this word.")
