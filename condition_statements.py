score = 30
#if statement
if score >=90:
    print("A")

#else statement
if score >=90:
    print("A")
else:
    print("F")

#elif statement

if score >=90:
    print("A")
elif score >=80:
    print("B")
else:
    print("F")

#elif elif statement

if score >=90:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
else:
    print("F")

#Nested if statement (if inside another if.. )
submitted_project = True

if score >=90:
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
else:
    print("F")

#connecting condition

if score >=90 and submitted_project:
    print("A+")
elif score >=90:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
else:
    print("F")

#More example
if score >=90 and submitted_project:
    print("A+")
elif score >=90:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score >=60 or submitted_project:
    print("D")
else:
    print("F")

#inline if
x= "A" if score >=90 else "Failed"
print(x)