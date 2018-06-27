import time

x = 0
y = 1
a = "^"
b = "_"
c = 30
d = "v"

while True:
    time.sleep(0.01)
    print((a*x) + (b*x) + d*10
          + (b * (c-x)) + (a * (c-x)))
    x = x + y
    if x == c or x == 0:
        y *= -1
    
