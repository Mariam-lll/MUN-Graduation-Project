import random
import string 

def create_pass():
    while True:
        length = input("The length of the required password: ")
        try:
            int(length)
            break
        except:
            print("Please enter a valid number.")
   
    print("Choose what to use in the password:\n1. Numbers \n2. Uppercase letters\n3. Lowercase letters\n4. Special characters")

    while True:
        chosens = input("Enter the numbers of the required elements: ").split(",")
        try:
            for i in chosens:
                i = int(i)
                if i not in [1, 2, 3, 4]:
                    raise ValueError
            break
        except:
            print("Please enter valid numbers within 1, 4")
        
    pass_arr = []
    for i in range(0, int(length)):
        choice = random.choice(chosens)
        if int(choice) == 1:
            pass_arr.append(str(random.randint(1, 9)))
        elif int(choice) == 2:
            pass_arr.append(random.choice(string.ascii_letters).upper())
        elif int(choice) == 3:
            pass_arr.append(random.choice(string.ascii_letters).lower())
        elif int(choice) == 4:
            pass_arr.append(random.choice(string.punctuation))
                
    return "".join(pass_arr)
        
        
def check_pass():
    password = input("Please enter the password: ")
    if len(password) < 8:
        print("The password should be at least 8 characters long.")
    check_arr = []
    result_arr = []
    for i in password:
        if i in string.ascii_letters.upper():
            check_arr.append("Capital")
        if i in string.ascii_letters.lower():
            check_arr.append("Small")
        if i.isdigit():
            check_arr.append("Number")
        if i in string.punctuation:
            check_arr.append("Special character")
    if "Capital" not in check_arr:
        result_arr.append("The password should contain at least 1 capital letter.")
    if "Small" not in check_arr:
        result_arr.append("The password should contain at least 1 small letter.")
    if "Number" not in check_arr:
        result_arr.append("The password should contain at least 1 number.")
    if "Special character" not in check_arr:
        result_arr.append("The password should contain at least 1 special character.")
    if len(result_arr) == 0:
        result_arr.append("The password is strong!")
    for i in result_arr:
        print(i)
        

print("Welcome to password hub!!\nWhich program would you like?\n1. Password creator\n2. Password strength checker")
while True:
        program = input("Enter the number of the program: ")
        try:
            int(program)
            if int(program) not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid number within 1, 2")
            
if program == "1":
   print(create_pass())
elif program == "2":
    check_pass()
print("Thanks for using password hub!!")    

