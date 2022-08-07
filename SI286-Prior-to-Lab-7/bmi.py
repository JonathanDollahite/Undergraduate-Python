# BMI calculator

print('How many feet tall are you?')
feet = int(input())
print('How many inches?')
inches = int(input())
height_in = (feet * 12) + inches
avg_man = (5 * 12) + 10
avg_wom = (5 * 12) + 4
avg_man_dif = abs(avg_man - height_in)
avg_wom_dif = abs(avg_wom - height_in)
print('You are', avg_man_dif, 'inches off from the average man')
print('You are', avg_wom_dif, 'inches off from the average woman')
print('How much do you weigh (in lbs)?')
weight = input()
weight = float(weight)
height_in = float(height_in)
bmi = (703 * (weight / (height_in * height_in)))
print('Your BMI is', bmi)
