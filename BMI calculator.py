#BMI Calc
name = input("What is your name?: ")
hight = float(input("What is your hight in meters?: "))
weight = float(input("What is your weight in kg?: "))

bmi_calc = (weight / (hight ** 2))
bmi = round(bmi_calc, 1)

if bmi < 18.5:
    print(f"Hi {name}, based on your current measurements your BMI of {bmi} indicates you are underweight.")

elif 18.5 <= bmi <= 24.9:
    print(f"Hi {name}, based on your current measurements your BMI of {bmi} indicates you are in the healthy range.")

elif  25 <= bmi <= 29.9:
    print(f"Hi {name}, based on your current measurements your BMI of {bmi} indicates you are overweight.")

elif 30 <= bmi <= 39.9:
    print(f"Hi {name}, based on your current measurements your BMI of {bmi} indicates you are obese.")

elif bmi >= 40:
    print(f"Hi {name}, based on your current measurements your BMI of {bmi} indicates you are severely obese.")