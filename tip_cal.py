print("Welcome to tip calculator!")
bill = float(input("What was the total bill?: "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
total_people = int(input("How many people to split the bill? "))

tip_percentage = tip / 100
total_tip = bill * tip_percentage
total_bill = bill + total_tip
split = (total_bill/total_people)
final = round(split, 2)
print(f"Each person should pay: {final}")



#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
# FAQ: How to round to 2 decimal places?
# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048

