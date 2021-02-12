"""Decompose conditional"""
# By Kami Bigdely
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
cholesterol = 70
ldl = 30 # low-density lipoprotein
tlc = 120 # triglyceride

if cholesterol < 200 and ldl < 100 and tlc < 150:
    # good level
    print('*** Good level of cholesterol ***')
elif 200 < cholesterol < 240 or 130 < ldl < 160 or 150 <= tlc < 200:
    # TLC_diet
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')
else:
    # High cholesterol level
    print('*** High cholesterol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')
