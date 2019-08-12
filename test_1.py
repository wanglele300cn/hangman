age = 64
retirement = age -65

if retirement < 10:
    print("you get to retire soon")
else:
    print("you have a long time until you can retire")

x="abc"
print("x=%s"%(x))

def div2(x,y):
    if y!=0:
        return x//y
    else:
        return "chushuwei0"

x = 10.2
y = 1.2
a = div2(x,y)
print(a)

def div(x,y):
    if y!=0:
        return x%y
    else:
        return "chushuwei0"
x = 10
y = 0
a = div(x,y)
print(a)

x = 15

if x<=10:
    print("<=10")
elif x<=25:
    print("10<x<=25")
else:
    print("x>25")

x = 10

if x<10:
    print("xioyudengyu10")
else:
    print("dayudengyu10")

print("hello,world!")
print("zhongguo,nihao!")
print("hi,beijing!")