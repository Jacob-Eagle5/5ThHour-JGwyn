#Name: Jacob Gwyn
#Class: 5th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

W = int(input("What's your weight in pounds:"))
H = int(input("What's your height in inches:"))
print("______________________________")

BMI_Results = 703 * (W/(H**2))

print(BMI_Results)
print("______________________________")
if BMI_Results < 18.5:
    print("Underweight")
elif BMI_Results >=18.5 and BMI_Results <=24.9:
    print("Normal")
elif BMI_Results >=25 and BMI_Results <=29.9:
    print("Overweight")
else:
    print("Obese")
