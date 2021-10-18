import sys

print("BMI: Body Mass Index Calculator v.0.1 beta")
userWeight = input("Enter your weight (in pound): ")
userHeight = input("Enter your Height (in inches): ")

myBMI = (703 * float(userWeight)) / pow(float(userHeight),2)
myBMI =round(myBMI,2)
print("you body mass index (BMI) is " + str(myBMI) + "%")