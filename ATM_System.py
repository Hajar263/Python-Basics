acc_number = (13456, 24685, 78925, 14359, 12345)
working_password = 1234
balance = 7000

def ATM():

    language = input("Enter Language: ")

    if language.lower() == "english":

        def number():
            num = input("Enter Account Number: ")
            tries = 3
            for i in range(3):
                if int(num) not in acc_number:
                    tries -= 1
                    print("Account Number is not Valid")
                    print(tries, "Tries Left")
                    if i != 2:
                        num = input("Enter Account Number: ")
                        continue
                    else:
                        quit()
                else:
                    print("Correct Number")
                    break

        number()

        def password():
            num = input("Enter your password: ")
            tries = 3
            for i in range(3):
                if int(num) != working_password:
                    tries -= 1
                    print("Password is Incorrect")
                    print(tries, "Tries Left")
                    if i != 2:
                        num = input("Enter Password: ")
                        continue
                    else:
                        quit()
                else:
                    print("Correct Password")
                    break


        password()


        # Withdraw / Deposit / Check Balance

        def oper():

            global balance
            operation = input("Enter Operation (withdraw / deposit / check balance): ")

            if operation.lower().replace(" ", "") == "withdraw":
                amount = int(input("How much money you want: "))
                while True:
                    if amount > balance:
                        print("Your balance is not enough")
                        amount = int(input("How much money you want: "))
                    elif amount <= balance:
                        print("Withdraw Successful")
                        balance -= amount
                        print("Balance now is ", balance)
                        break

            elif operation.lower().replace(" ", "") == "deposit":

                amount = int(input("How much money you want to deposit: "))
                print("Deposit Successful")
                balance += amount
                print(balance, "now")

            elif operation.lower().replace(" ", "") == "checkbalance":
                print(balance)

            else:
                print("Operation Unknown, please try again")
                oper()

        while True:
            oper()
            var = input("Do you want to continue: ")
            if var.lower() == "yes":
                continue
            elif var.lower() == "no":
                print("Thank you, see you soon!")
                quit()
            else:
                var = input("Choose yes / no: ")


    elif language == "عربي":

        def number():
            num = input("ادخل رقم الحساب : ")
            tries = 3
            for i in range(3):
                if int(num) not in acc_number:
                    tries -= 1
                    print("رقم الحساب غير صالح")
                    print(tries, "المحاولات المتبقية")
                    if i != 2:
                        num = input("ادخل رقم الحساب : ")
                        continue
                    else:
                        quit()
                else:
                    print("الرقم صحيح")
                    break


        number()

        def password():
            num = input("ادخل كلمة السر: ")
            tries = 3
            for i in range(3):
                if int(num) != working_password:
                    tries -= 1
                    print("كلمة السر غير صحيحة")
                    print(tries, "المحاولات المتبقية")
                    if i != 2:
                        num = input("ادخل كلمة السر: ")
                        continue
                    else:
                        quit()
                else:
                    print("كلمة السر صحيحة")
                    break


        password()

        # سحب / ايداع / معرفة الرصيد

        def oper():

            global balance
            operation = input("(سحب \ إيداع \ معرفة الرصيد) أدخل العملية: ")

            if operation.replace(" ", "") == "سحب":
                amount = int(input("كم تريد: "))
                while True:
                    if amount > balance:
                        print("لا يوجد رصيد كافي")
                        amount = int(input("كم تريد: "))
                    elif amount <= balance:
                        print("تمت عملية السحب")
                        balance -= amount
                        print("رصيدك الان, ", balance)
                        break

            elif operation.replace(" ", "") == "إيداع":

                amount = int(input("كم تريد أن تودع: "))
                print("تمت عملية الإيداع")
                balance = balance + amount
                print(balance, "الان")

            elif operation.replace(" ", "") == "معرفة الرصيد":
                print(balance)

            else:
                print("عملية غير معروفة, حاول مجددا")
                oper()

        while True:
            oper()
            var = input("هل ترغب في إكمال العملية: ")
            if var.lower() == "نعم":
                continue
            elif var.lower() == "لا":
                print("شكرا لك, نراك قريبا")
                quit()
            else:
                var = input("إختر نعم / لا: ")

    else:
        print("Unidentified Language, please try again")
        ATM()

ATM()
