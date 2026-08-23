tup = (1,2,3,4,5,6,7,8,9)
target = int(input("Enter a number bw 1-9: "))
i = 0
while i < len(tup):
    if tup[i] == target:
        print("Found:",target)
        break
    i+=1