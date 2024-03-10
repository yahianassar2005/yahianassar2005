# Authors:
 
# Author 1 : حمزه عمر سعد  - 20230127
#solved tasks :task 2 -task 4


# Author 2 :يحيى محمد عادل نصار - 202312066
# solved tasks : task 3- task 5


# Author 3 : 20230569-عمر محمد محمد سيد مصطفى
# solved tasks : task 1 - task 6 

# version 1

# Date: 24-2-2024

def task_1():
    # program Description : program that convert the numerical grade into a alphabitical grade  
    mark = float(input("Enter yout mark : "))
    if mark >= 95 :
        print("Your mark is ",mark,  "your grade is A+")
    elif mark >= 90:
        print("Your mark is ",mark,  "your grade is A")
    elif mark >= 80 :
        print("Your mark is ",mark, "your grade is A-")
    elif mark >= 80:
        print("Your mark is ",mark, "your grade is B+")
    elif mark >= 75:
        print("Your mark is ",mark, "your grade is B")
    elif mark >= 70:
        print("Your mark is ",mark, "your grade is B-")
    elif mark >= 65:
        print("Your mark is ",mark, "your grade is C+")
    elif mark >= 60:
        print("Your mark is ",mark, "your grade is C")
    elif mark >= 55:
        print("Your mark is ",mark, "your grade is C-")
    elif mark >= 50:
        print("Your mark is ",mark, "your grade is D+")
    elif mark >= 45:
        print("Your mark is ",mark, "your grade is D")
    elif mark >= 40:
        print("Your mark is ",mark, "your grade is D-")
    else:
        print("Your mark is ",mark, "your grade is F")
def task_2():
    #  program Description : program to check whether a given number is an Armstrong number or not 
    # a positive int is said to be an Armstrong number:
    # if the sum of  individual digits raised to the power of number of  digits  is equal to that number itself 

    num=int(input("enter the num "))
    # make the input number a string to know its length
    str_num=str(num)

    no_of_digits=len(str_num)
    # setting the intial value of sum 
    summation=0

    for  digits in str_num:

        summation+=int(digits)**no_of_digits
    #checking whether the sum equal thr number or not
    if summation==num:

        print('the number is armstrong num') 
        
    else :
        print("num is not an armstrong number")   

    print("="*50)     

def task_3():
#  program Description :calculating pi using the german's mathematician Leibniz method

    print("##Leibniz Game##")
    n = int(input("please enter the number of terms to calculating pi"))
    denomenator = 1 #intial value
    result = 0
    for i in range(n):
        nums = 1 * ((-1) ** i) / denomenator
        result += nums
        i += 1
        denomenator = denomenator + 2
    print(result * 4)

def task_4():
#  program Description :Encryption by  using Casar cipher wheere it is  shifting each character to the next one.
    
    message= input('enter the  message ')
    
    for char in message :

        shift_value = 1

        # turning character into its number in ASCII
        original_char_code = ord(char)
        # adding shifted value to character code
        shifted_char_code = original_char_code + shift_value
        # returning character after encrypting 
        shifted_char = chr(shifted_char_code)
        # adjusting the code output 
        if char ==" ":
            shifted_char=" "

        if char =="z":
            shifted_char="a"

        if char =="Z":
            shifted_char="A"
 
            
        print(shifted_char, end="")

    print()     
    print("="*50)   
# task 5
 #  program Description :compering two lists and stating wether they are equal or not       
def task_5():
    print("##list compare##")
    def arrange_list(the_list):
        
        for i in range(0, len(the_list)):
            for j in range(i+1, len(the_list)):
                if the_list[i] >= the_list[j]:
                    # temporary variable
                    temp = the_list[i]
                    the_list[i] = the_list[j]
                    the_list[j] = temp

        return(the_list)
    def input_filter(the_list):
        for char in the_list:
            if char=="["or char=="]"or char == ",":
                continue 


    list_one =list(input('enter the 1st list items  '))

    list_two =list(input('enter the 2nd list items  '))
    input_filter(list_one)
    input_filter(list_two)
    list_one_arranged=arrange_list(list_one)
    list_two_arranged=arrange_list(list_two)

    if len(list_one)!= len(list_two):
        print("CANNOT COMPERE LENGH IS NOT THE SAME ENTER THE LISTS AGAIN")
        list_one =list(input('enter the 1st list items  '))
        list_two =list(input('enter the 2nd list items '))

    if list_one_arranged==list_two_arranged:
        print("list are equal = True")
    else: 
        print("list are not  = False")    


def task_6():
# program Description :  give the factors of the number and represent it in a list
    print("## Factors Generator ##")
    number = int(input("Enter the number: "))

    factors_list = []

    for divisor in range(1, number + 1):

        if number % divisor == 0:

            factors_list.append(divisor)

            
        factors_list.sort()
    print(f"Factors of{number} are: {factors_list }")

while True:
    print("=>group task menue<=")
    print("1) task 1 \n2) task 2 \n3) task 3 \n4) task 4 \n5) task 5 \n6) task 6 \n 7) exit the program ")
    choice=int(input("enter the choice"))
    if choice==1:
        task_1()
    elif choice==2:
        task_2()
    elif choice==3:
        task_3()
    elif choice==4:
        task_4()
    elif choice==5:
        task_5()
    elif choice==6:
        task_6()
    elif choice==7: 
        print("exiting the program")  
        break 
    else:
        print("enter a valid choice")
