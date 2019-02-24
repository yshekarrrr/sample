def add(a,b):
    print("The Sum is %d" %(a + b))

def sub(a,b):
    print("The Sub is %d" % (a - b))

def mul(a,b):
    print("The Mul is %d" % (a * b))

def div(a,b):
    print("The Div is %d" % (a // b))

a = int(input("please enter the value of 'a' :"))
b = int(input("please enter the value of 'b' :"))
add(a,b)
sub(a,b)
mul(a,b)
div(a,b)
input("press enter to exit")