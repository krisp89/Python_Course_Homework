# Calculate your body mass index (BMI) with Python, given the formula:
# BMI = W / (H*H)
# where:
# W = weight_in_kilogram
# H = height_in_meters
# Your program should outputs the result rounded to 2 digits after the decimal point).
# Try to think of a solution, which will be readable enough and easy to maintain in future (you can use comments and semantic variable names)
# write your code in HW/BMI.py file
# Tip: You can use the python's build-in round() function, like:
# >>> round(2.1457, 2)
# 2.15

# >>> round(1.4234,2)
# 1.42

# >>> round(1.4284,2)
# 1.43

weight = 94
height = 1.79
BMI=weight/(height*height)
# Instead of rounding the result as susggested in the presentation, I used the f string to round it up to the second number after the decimal point
print(f'{BMI:.2f}')