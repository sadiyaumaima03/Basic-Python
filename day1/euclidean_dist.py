import math
x1 = 2
x2 = 3
y1 = 10
y2 = 8
#(x2 - x1), (y2 - y1); 
A = (x2 - x1) 
B = (y2 - y1)
#squaring em using exponential operator then suming those values &sqroot to get distance.
distance = math.sqrt((A ** 2) + (B ** 2))
print(f'Distance = {distance}')