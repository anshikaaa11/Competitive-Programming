angle1 = int(input("enter the first angle"))
angle2 = int(input("enter the second angle"))
angle3 = int(input("enter the third angle"))

if angle1 == 180:
    print("triangle is right triangle")
elif angle2 == 90:
    print("triangle is obtuse triangle")
else:
    print("triangle is actue angle")