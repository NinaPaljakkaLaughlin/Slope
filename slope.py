x1 = float(input("Input x1:"))
x2 = float(input("Input x2:"))
y1 = float(input("Input y1:"))
y2 = float(input("Input y2:"))

if x2 - x1 == 0:
    print("vertical line")
else:
    slope = ( (y2 - y1) / (x2 - x1) )
    if slope < 0:
        print("Negative slope")
    if slope > 0:
        print("Positive slope")
    if slope == 0:
        print("Horizontal line")

