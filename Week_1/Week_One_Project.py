print("Hello👋 and welcome to your calculator")

print("I see you want to carry out a calculation. "
      "\n Here are services we offer \n\t Simple Interest \n\t Compound Interest \n\t Annuity Plan")

print("before we continue please input your variables ")
#Var_P is the variable or P the int is to convert Var_P into an integer input
var_P = input("\tInput variable for P___")
var_P = int(var_P)

#Var_R is the variable or R the int is to convert Var_R into an integer input
var_R = input("\t Input variable for R___")
var_R = int(var_R)

#Var_T is the variable or T the int is to convert Var_T into an integer input
var_T = input("\t Input variable for T___")
var_T = int(var_T)

#Var_N is the variable or N the int is to convert Var_N into an integer input
var_N = input("\t Input variable for N___")
var_N = int(var_N)

#Var_PMT is the variable or PMT the int is to convert Var_PMT into an integer input
var_PMT = input("\t Input variable for PMT___")
var_PMT = int(var_PMT)

print("To continue pick a service. \n\t 1--- Simple Interest "
      "\n\t 2 --- Compound Interest \n\t 3 --- Annuity Plan")
choice_main = input("\tPlease make a choice -- ")
choice_main = int(choice_main)

if choice_main == 1:
    print("Option is loading ***** \nYou selected Simple Interest")
    solution_optA = var_P * (1 + (var_R / 100) * var_T)
    print (f"Your simple interest is  {solution_optA}")
elif choice_main == 2:
    print("Option is loading **** \n You selected Compound Interest")
    solution_optB = var_P * (1 + (var_R / var_N)) ** (var_T * var_N)
    solution_optB = int(solution_optB)
    print(f"Your compound interest is {solution_optB}")
else :
    print("Option is loading ***** \n You selected Annuity Plan")
    solution_optC = var_PMT * ((1 + (var_R / var_N)) ** (var_T * var_N) - 1/ (var_R / var_N) )
    print(f"Your Annuity Plan is {solution_optC}")




