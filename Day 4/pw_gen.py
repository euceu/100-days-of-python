import secrets
import os

def new_password():
    ask_new_pw = input('Do you want to generate a new password? Type "yes" or "no": ')
    if ask_new_pw.lower() == "no":
        exit()
    elif ask_new_pw.lower() == "yes":
        pw = (secrets.token_urlsafe(nbytes=8))
        print(pw)

        def pw_confirm():
            ask_input = input('Is this password ok? Type "yes" or "no": ')
            if ask_input.lower() == "yes":
                os.system('clear')
                exit()
            elif ask_input.lower() == "no":
                print(secrets.token_urlsafe(nbytes=8))
                pw_confirm()
            else:
                print("Input invalid. Try again.")
                pw_confirm()

        pw_confirm()

    else:
        print("Input invalid. Try again.")
        new_password()


new_password()
