# Joshua Ryan Harris
# if...else and while
# Gets the name of the student, GPA. If it is equal to or higher than 3.5, it'll say you made both the Dean's List and the Honor Roll, buy only Honor Roll for 3.25 and above. Neither of lower than both. If ZZZ is typed for the students last name, it'll cancel out.
LName = ""
while LName != "ZZZ":
    LName = input("Enter student's last name: ")
    if LName == "ZZZ":
        break
    else:
        FName = input("Enter student's first name: ")
        Grade = float(input("Enter student's GPA: "))
    if Grade >= 3.5:
        print(FName, LName, "has made both the Dean's List and Honor Roll!")
    elif Grade >= 3.25:
        print(FName, LName, "has made the Honor Roll!")
    else:
        print(FName, LName, "has not made the Dean's List or Honor Roll")