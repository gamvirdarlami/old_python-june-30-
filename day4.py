name = input("enter students name:")
com = float(input("enter com marks:"))
math = float(input("enter math marks:"))
opt_maths = float(input("enter opt_maths marks:"))
nepali = float(input("enter nepali marks:"))
total = com + math + opt_maths + english + nepali
percentage = (total/500)*100
if percentage >= 90:
    print(f"congratulation {name} . your percentage is {percentage}")
elif percentage >= 80:
    print(f"congratulation {name} . your percentage is {percentage}")
elif percentage >= 70:
    print(f"congratulation {name} . your percentage is {percentage}")
elif percentage >= 60:
    print(f"congratulation {name} . your percentage is {percentage}")
elif percentage >= 50:
    print(f"congratulation {name} . your percentage is {percentage}")
elif percentage >= 40:
    print(f"congratulation {name} . your percentage is {percentage}")
else:
    print(f"sorry you have failed {name} . your percentage is {percentage}")