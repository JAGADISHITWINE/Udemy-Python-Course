## SI = P * N * R / 100

principle = int(input("Enter the amount borrowed "))
years = float(input("Enter the period in years "))
rate = float(input("Enter the Rate of Interest "))

interest = (principle * years * rate)/100
print(f"Simple Interest on the {principle}$ for the period of {years} years at the rate of {rate}% is {interest}$")
