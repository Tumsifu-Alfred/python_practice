#CONTROL FLOW STATEMENTS IN PYTHON
 #---Conditional statement
 #---Loops

#BOOLEANS 
print(True)
print(False)
print(type(True))
print(bool(123))
print(bool("kamala"))
print(bool()) #Returns false because its empty

print(7>5)
print("a">"b")
print(10 == 10)
print(1<4<5)
print(len("Hello") == 5)

#Assignment operator vs comparison operayor
#Assignment(=) Comparison(==)

#LOGICAL OPERATORS
#Used to evaluate multiple conditions
#and (both conditions must be true) | or (Atleast one condition is true) | Not (Flips the truth)

print("Logical")
print(3>2 and 4<5)
print(3>2 and 4>5)
print(3>2 or 4>5)

email = True 
password = False

print(email and password) #Both must be true for the user to login

print(not True)
print(not False)

#When all logical operators are used together "and"operator has more priority than "or"
print(5==5 or 8>5 and 6<4) #prove
print((5==5 or 8>5) and 6<4) #Having a control over the reality so, condition in brackets will be executed first

#End at 4:02