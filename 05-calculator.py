a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
op=input("Enter operation(+ - * /):")
if op=="+":
 print("sum:",a+b)
elif op=="-":
 print("sub:",a-b)
elif op=="*":
 print("Mul:",a*b)
elif op=="/":
 print("div:",a/b)
else:
 print("invalid operation")
