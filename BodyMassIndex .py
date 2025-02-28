#Exercise 3
#BodyMassIndex

Weight=float(input("Enter your weight(kg): "))
Height=float(input("Enter your height(m): "))

BMI= Weight/(Height**2)
print(f" Your BMI is:{BMI}")
if BMI<18.5:
    print('You are in the "underweight" range.')
elif 18.5<= BMI <= 24.9:
    print('You are in the "Normal" range.')
elif 25 <= BMI <= 29.9:
    print('You are in the "overweight" range.')
else:
    print('You are in the "obese" range.')