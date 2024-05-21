## BMI = weight in kgs / (height in m)^2

weight = float(input("Enter the weight in kgs: "))
height = float(input("Enter the height in m: "))

BMI = weight / (height ** 2 )
print(f'The BMI for {weight} kg and {height} m is {BMI}')
