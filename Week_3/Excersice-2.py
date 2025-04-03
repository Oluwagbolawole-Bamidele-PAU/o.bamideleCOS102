#Code solution for Project II
#If the staff work_year > 25 && age >= 55, ATR = 5,600,000
#If staff : work_year > 20 && age >= 45, ATR = 4,480,000
#if staff : work_year >10 && age is >= 35, ATR = 1,500,000
#if staff : work_year < 10 && age < 35, ATR = 550,000

print("Welcome Employee")
staff_age = input("Please what's your age")
staff_age = int(staff_age)

staff_exp = input("Please what's your working expirence")
staff_exp = int(staff_exp)

if staff_exp > 25 and staff_age >= 55:
    atr = 5_600_000
elif staff_exp > 20 and staff_age >= 45:
    atr = 4_480_000
elif staff_exp > 10 and staff_age >= 35:
    atr = 1_500_000
elif staff_exp < 10 and staff_age < 35:
    atr = 550_000
else:
    atr = "???"

print("ANNUAL TAX REVENUE FOR THE STAFF IS :   ", atr)