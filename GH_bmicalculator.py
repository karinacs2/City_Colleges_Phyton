# Body mass index (BMI) Calculator

# Input weight and height
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

# BMI Calculation
bmi = weight / (height ** 2)
print(bmi)

# Results
if bmi < 18.5:
    print("Underweight")
    print("Seek assistance!")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
    print("Keep it up!")
elif 25 <= bmi < 29.9:
    print("Overweight")
    print("Take action!")
else:
    print("Obesity")
    print("Prioritize your health!")
