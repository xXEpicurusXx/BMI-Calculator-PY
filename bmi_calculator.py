# 🚨 Don't change the code below 👇
height = float(input("enter your height in cm: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆


#Write your code below this line 👇
height2 = float(height) * .01

bmi = float(weight) / (float(height2) ** 2)
round_bmi = round(bmi)

if bmi <= 18.5:
    print(f"Your BMI is {round_bmi}, you are underweight")
elif bmi <= 24:
    print(f"Your BMI is {round_bmi}, you have a normal weight.")
elif bmi <= 29:
    print(f"Your BMI is {round_bmi}, you are slightly overweight")
elif bmi <= 34:
    print(f"Your BMI is {round_bmi}, you are obese")
elif bmi >35:
    print(f"Your BMI is {round_bmi}, you are clinically obese.")

