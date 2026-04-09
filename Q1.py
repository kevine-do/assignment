checking_grade = float(input("enter your marks:"))

if checking_grade >=80:
    print("distinction")
elif checking_grade >=60 and checking_grade<=79:
    print("credit")
    
elif checking_grade>=50 and checking_grade<=59:
    print("pass")
else:
    print("fail")

